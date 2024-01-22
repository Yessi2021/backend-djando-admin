# En el archivo myapp/serializers.py
from rest_framework import serializers
from .models import Configuration
from bi360.business.models import Business


class ConfigurationSerializer(serializers.ModelSerializer):
    related_model = serializers.PrimaryKeyRelatedField(queryset=Business.objects.all())

    # columns_mapping_json = serializers.JSONField(source='columns_mapping', read_only=True)

    class Meta:
        model = Configuration
        fields = '__all__'

    # def to_representation(self, instance):
    #     # representation = super().to_representation(instance)
    #     representation['columns_mapping'] = instance.columns_mapping  
