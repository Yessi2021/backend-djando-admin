
from rest_framework import generics
from .models import Configuration
from .serializers import ConfigurationSerializer

class ConfigurationList(generics.ListCreateAPIView):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer

class ConfigurationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer