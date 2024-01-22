from django.urls import path

from .views import ConfigurationList

app_name = "upload"

urlpatterns = [
    path("upload/", ConfigurationList.as_view(), name="upload"),
]
