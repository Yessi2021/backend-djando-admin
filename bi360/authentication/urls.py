from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import PasswordRecoveryView, PasswordResetView, UserBusinessCreateAPIView

app_name = "auth"

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token-verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("password-recovery/", PasswordRecoveryView.as_view(), name="password_recovery"),
    path("change-password/", PasswordResetView.as_view(), name="change_password"),
    # Request demo
    path("request-demo/", UserBusinessCreateAPIView.as_view(), name="request_demo"),
]
