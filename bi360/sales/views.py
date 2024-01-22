import pandas as pd

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from bi360.business.models import Business
from bi360.core.utils.get_df_from_request import get_df_from_request
from bi360.core.utils.save_df_in_db import save_df_in_db
from bi360.upload_setup.models import Configuration

from .models import Sale
from .serializers import SaleSerializer


class SaleFieldInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        field_info = [{
            "field_name": field.name,
            "verbose_name": getattr(field, "verbose_name", field.name),
        } for field in Sale._meta.fields if field.name not in ["id", "business"]]
        return Response({"field_info": field_info})


class StorageExcel(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            df = get_df_from_request(request.data)
            # Leemos el archivo con Pandas
            if df is None:
                return Response({"error": "El archivo no existe"}, status=status.HTTP_404_NOT_FOUND)
            # Obtiene la instancia de Business con la clave primaria (PK) 1
            business_instance = Business.objects.get(pk=1)
            df["business_id"] = business_instance.id

            # format date column
            df = df.dropna(subset=["sale_date"])
            df["sale_date"] = pd.to_datetime(df["sale_date"], format="%d/%m/%Y")

            # Reemplaza valores vacíos en columnas numéricas con 0
            numeric_columns = ["quantity", "unit_price", "discount_value"]
            df[numeric_columns] = df[numeric_columns].fillna(0)

            # Ajustar cualquier valor menor a 0 en 0
            df["quantity"] = df["quantity"].apply(lambda x: max(x, 0))

            # Remover duplicados
            df["transaction_id"] = df["transaction_id"].astype(str)
            df["transaction_id"] = (
                df["business_id"].astype(str) + "_" + df["sale_date"].dt.strftime("%Y%m%d") + "_" +
                df["transaction_id"]
            )
            df = df.drop_duplicates(subset="transaction_id", keep="first")
            existing_sales = Sale.objects.filter(business=business_instance).values_list("transaction_id", flat=True)
            df = df[~df["transaction_id"].isin(existing_sales)]
            save_df_in_db(df, Sale._meta.db_table)
            # Remover el archivo
            # os.remove(full_path)
            config =  Configuration.objects.Create(related_model=business_instance,selected_sheet=request.data.get("sheetName"), headers_index=request.data.get("sheetIndex"),columns_mapping=request.data.get("mapping"),destination_table="sales",name=request.data.get(""))


     

            return Response({"status": "Procesamiento exitoso"}, status=status.HTTP_200_OK)
        except Exception as e:
            # En caso de excepción, devolvemos un error
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BusinessSales(APIView):

    def get(self, request, business_id):
        try:
            # Obtiene la instancia de Business por su pk (que es 'business_id' en este caso)
            business = Business.objects.get(pk=business_id)

            # Obtiene todas las ventas asociadas a ese negocio
            sales = Sale.objects.filter(business=business)

            # Serializa los datos de las ventas
            serializer = SaleSerializer(sales, many=True)

            # Devuelve los datos serializados
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Business.DoesNotExist:
            return Response({"error": "Negocio no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
