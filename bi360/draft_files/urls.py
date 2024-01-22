from django.urls import path

from .views import CheckExcel

app_name = "draft"

urlpatterns = [
    path("check-excel/", CheckExcel.as_view(), name="verify_excel"),
]
