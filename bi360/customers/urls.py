from django.urls import path

from .views import ContactView, CustomerFieldInfoView, StorageExcel, ValuationView

app_name = "customer"

urlpatterns = [
    path("fields-info/", CustomerFieldInfoView.as_view(), name="fields-info"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("valuation/", ValuationView.as_view(), name="valuation"),
    path("save/", StorageExcel.as_view(), name="upload_excel"),
]
