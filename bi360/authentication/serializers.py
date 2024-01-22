from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # Convert email to lowercase
        attrs["email"] = attrs["email"].lower()

        # Check if the user is active
        user = User.objects.get(email=attrs["email"])
        if not user.is_active:
            raise AuthenticationFailed(
                detail="Por favor comuníquese con el administrador del sistema\
.",
                code="inactive_user",
            )

        # Call the parent's validate method
        validated_data = super().validate(attrs)
        return validated_data
