from django.urls import path

from .views import ProductsFieldInfoView, StorageExcel

app_name = "products"

urlpatterns = [
    path("fields-info/", ProductsFieldInfoView.as_view(), name="fields-info"),
    path("save/", StorageExcel.as_view(), name="upload_excel"),
]
