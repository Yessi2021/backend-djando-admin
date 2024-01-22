from rest_framework import serializers

from .models import Sale


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = "__all__"
        # Si solo necesitas algunos campos, puedes especificarlos en una lista:
        # fields = ['sale_date', 'product_code', 'customer_code', 'amount', 'product_quantity',
        #  'discount', 'final_value', 'is_successful']
