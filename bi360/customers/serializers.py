from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    business = serializers.CharField()
    phone = serializers.CharField(required=False, allow_blank=True)
    message = serializers.CharField()


class ValuationSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    business = serializers.CharField()
    tools = serializers.IntegerField(required=False, allow_null=True)
    standars = serializers.IntegerField(required=False, allow_null=True)
    avaliability = serializers.IntegerField(required=False, allow_null=True)
    level = serializers.IntegerField(required=False, allow_null=True)
    management = serializers.IntegerField(required=False, allow_null=True)
