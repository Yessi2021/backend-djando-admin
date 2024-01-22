from django.contrib import admin
from django.urls import include, path

API_PREFIX = "api/v1/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{API_PREFIX}auth/", include("bi360.authentication.urls")),
    path(f"{API_PREFIX}customer/", include("bi360.customers.urls")),
    path(f"{API_PREFIX}draft/", include("bi360.draft_files.urls")),
    path(f"{API_PREFIX}payroll/", include("bi360.payroll.urls")),
    path(f"{API_PREFIX}powerbi/", include("bi360.powerbi_auth.urls")),
    path(f"{API_PREFIX}products/", include("bi360.products.urls")),
    path(f"{API_PREFIX}sales/", include("bi360.sales.urls")),
    path(f"{API_PREFIX}upload/", include("bi360.upload_setup.urls")),
]
