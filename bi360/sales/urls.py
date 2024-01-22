from django.urls import path

from .views import BusinessSales, SaleFieldInfoView, StorageExcel

app_name = "sales"

urlpatterns = [
    path("fields-info/", SaleFieldInfoView.as_view(), name="fields-info"),
    path("save/", StorageExcel.as_view(), name="upload_excel"),
    path("<int:business_id>/", BusinessSales.as_view(), name="business-sales"),
]
