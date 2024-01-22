from django.urls import path

from .views import PowerBIAPIView

app_name = "powerbi"

urlpatterns = [
    path("auth-token/", PowerBIAPIView.as_view(), name="auth_token"),
]
