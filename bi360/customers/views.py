from datetime import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bi360.business.models import Business
from bi360.core.utils.get_df_from_request import get_df_from_request
from bi360.core.utils.save_df_in_db import save_df_in_db

from .models import Contact, Customer, EndCustomer, Valuation
from .serializers import ContactSerializer, ValuationSerializer


class CustomerFieldInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        field_info = [{
            "field_name": field.name,
            "verbose_name": getattr(field, "verbose_name", field.name),
        } for field in EndCustomer._meta.fields if field.name not in ["id", "is_successful", "business"]]
        return Response({"field_info": field_info})


# Create your views here.
class ContactView(APIView):

    def post(self, request):
        serializer = ContactSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            name = serializer.validated_data.get("name")
            business = serializer.validated_data.get("business")
            phone = serializer.validated_data.get("phone")
            message = serializer.validated_data.get("message")

            try:
                user = Customer.objects.get(email=email)
            except Customer.DoesNotExist:
                user = Customer(email=email, date_joined=datetime.now())

            user.name = name
            user.business = business
            user.is_active = True
            if phone:
                if user.phone and user.phone != phone:
                    user.phone1 = user.phone
                user.phone = phone

            user.save()

            new_msg = Contact(
                customer=user,
                created_at=datetime.now(),
                is_active=True,
                message=message,
            )
            new_msg.save()

            response_data = {
                "message": "Pronto estaremos en contacto contigo",
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValuationView(APIView):

    def post(self, request):
        serializer = ValuationSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            name = serializer.validated_data.get("name")
            business = serializer.validated_data.get("business")
            tools = serializer.validated_data.get("tools")
            standars = serializer.validated_data.get("standars")
            avaliability = serializer.validated_data.get("avaliability")
            level = serializer.validated_data.get("level")
            management = serializer.validated_data.get("management")

            try:
                user = Customer.objects.get(email=email)
            except Customer.DoesNotExist:
                user = Customer(email=email, date_joined=datetime.now())

            user.name = name
            user.business = business
            user.is_active = True

            user.save()

            new_valuation = Valuation(
                customer=user,
                created_at=datetime.now(),
                business=business,
                tools=tools,
                standars=standars,
                avaliability=avaliability,
                level=level,
                management=management,
            )
            new_valuation.save()

            response_data = {
                "message": "Valoración almacenada exitosamente",
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StorageExcel(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            df = get_df_from_request(request.data)
            # Leemos el archivo con Pandas
            if df is None:
                return Response({"error": "El archivo no existe"}, status=status.HTTP_404_NOT_FOUND)
            # Obtiene la instancia de Business con la clave primaria (PK) 1
            business_instance = Business.objects.get(pk=1)
            df["business_id"] = business_instance.id

            # delete rows where 'sku' is NaN
            df = df.dropna(subset=["customer_code"])
            df = df.dropna(subset=["name"])

            # Remove duplicates or assign new SKUs as appropriate
            df["customer_code"] = df["customer_code"].astype(str)
            df = df.drop_duplicates(subset="customer_code", keep="first")
            existing_skus = EndCustomer.objects.values_list("customer_code", flat=True)
            df = df[~df["customer_code"].isin(existing_skus)]
            save_df_in_db(df, EndCustomer._meta.db_table)
            # Remover el archivo
            # os.remove(full_path)

            return Response({"status": "Procesamiento exitoso"}, status=status.HTTP_200_OK)
        except Exception as e:
            # En caso de excepción, devolvemos un error
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
