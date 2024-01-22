from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken

from bi360.business.models import Business, UserBusinessRelationship
from bi360.core.utils.send_mail.send_mail import send_mail_to

from .models import User


# Create your views here.
class PasswordRecoveryView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if email is None:
            return Response(
                {"message": "El correo electrónico es obligatorio"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(email=email)
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            # Assuming the frontend URL is passed in the request headers
            frontend_url = request.headers.get("Referer", "https://bi360.com.co/")
            recovery_link = f"{frontend_url}recovery/change/{token}"

            # Call the hypothetical send_mail_to() function
            body = f"""
                <p>Hola <strong>{user.first_name} {user.last_name}</strong>,</p>
                <p>
                    Has solicitado restablecer tu contraseña. Por favor, haz clic en el botón de abajo en los próximos
                    10 minutos para establecer una nueva.
                </p>
                <a href="{recovery_link}" class="button" target="_blank"
                    >Restablecer contraseña</a
                >
            """
            send_mail_to("Recuperación de contraseña", body, [user.email])
            return Response(
                {"message": "Si el correo está registrado, se enviarán las instrucciones de recuperación"},
                status=status.HTTP_200_OK,
            )

        except User.DoesNotExist:
            return Response(
                {"message": "Si el correo está registrado, se enviarán las instrucciones de recuperación"},
                status=status.HTTP_200_OK,
            )


class PasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        token = request.data.get("token")
        password1 = request.data.get("password1")
        password2 = request.data.get("password2")

        if not token:
            return Response(
                {"message": "El token es obligatorio"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if password1 != password2:
            return Response(
                {"message": "Las contraseñas no coinciden"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            decode_token = UntypedToken(token)
            user_id = decode_token["user_id"]
            iat = decode_token["iat"]
            exp = decode_token["exp"]

            token_lifetime = 60 * 60 * 12
            token_lifetime_left = exp - iat
            if 0 > (token_lifetime - token_lifetime_left) < 600:
                return Response(
                    {"message": "Token expiró. Intentalo nuevamente"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user = User.objects.get(id=user_id)
            user.set_password(password1)
            user.save()

            return Response(
                {"message": "Contraseña actualizada con exito, ingresa nuevamente"},
                status=status.HTTP_200_OK,
            )

        except (TokenError, User.DoesNotExist) as e:
            print(e)
            return Response(
                {"message": "Token inválido o usuario erróneo"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserBusinessCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Retrieve user information from request
        try:
            with transaction.atomic():
                email = request.data.get("email", "").lower()
                nombre = request.data.get("nombre", "")
                password = get_random_string(length=8)

                # Retrieve business information from request
                n_empresa = request.data.get("nEmpresa", "")
                nit_empresa = request.data.get("nitEmpresa", "")
                telefono_empresa = request.data.get("telefonoEmpresa", "")

                # Create user
                user = User.objects.create_user(email=email, password=password, first_name=nombre)

                # Create business and associate it with the user
                business = Business.objects.create(name=n_empresa, nit=nit_empresa, phone=telefono_empresa)
                print(user.id, business.id)
                UserBusinessRelationship.objects.create(
                    user=user,
                    business=business,
                )

            # body
            frontend_url = request.headers.get("Referer", "https://bi360.com.co/")
            login_link = f"{frontend_url}login"
            body = f"""
                <p>Hola <strong>{user.first_name}</strong>,</p>
                <p>
                    Tu cuenta en nuestra plataforma ha sido creada exitosamente.
                    Aquí están tus credenciales para iniciar sesión:
                </p>
                <p>
                    Usuario: {user.email}<br>
                    Contraseña: {password}
                </p>
                <p>
                    Por favor, haz clic en el botón de abajo para ir a la página de inicio de sesión y
                    acceder a tu nueva cuenta.
                </p>
                <a href="{login_link}" class="button" target="_blank">Iniciar sesión</a>
            """

            # Send email with the generated password
            send_mail_to(
                "Bienvenido a BI360",
                body,
                [email],
                fail_silently=False,
            )

            return Response(
                {"status": "El registro ha sido exitoso"},
                status=status.HTTP_201_CREATED,
            )
        except IntegrityError as e:
            print(e)
            return Response(
                {"error": "Este correo ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ValidationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
