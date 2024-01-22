from django.urls import path

from .views import PayrollFieldInfoView, StorageExcel

app_name = "payroll"

urlpatterns = [
    path("fields-info/", PayrollFieldInfoView.as_view(), name="fields-info"),
    path("save/", StorageExcel.as_view(), name="upload_excel"),
]
