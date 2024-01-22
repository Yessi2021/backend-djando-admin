from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bi360.business.models import Business
from bi360.core.utils.get_df_from_request import get_df_from_request
from bi360.core.utils.save_df_in_db import save_df_in_db

from .models import Employee


class PayrollFieldInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        field_info = [{
            "field_name": field.name,
            "verbose_name": getattr(field, "verbose_name", field.name),
        } for field in Employee._meta.fields if field.name not in ["id", "is_available", "business"]]
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
            # Reemplaza valores vacíos en columnas numéricas con 0
            numeric_columns = ["salary"]
            df[numeric_columns] = df[numeric_columns].fillna(0)

            # Elimina filas donde 'sku' es NaN
            df = df.dropna(subset=["employee_id"])
            df = df.dropna(subset=["first_name"])
            df = df.dropna(subset=["salary"])

            # Remove duplicates or assign new SKUs as appropriate
            df["employee_id"] = df["employee_id"].astype(str)
            df = df.drop_duplicates(subset="employee_id", keep="first")
            existing_skus = Employee.objects.values_list("employee_id", flat=True)
            df = df[~df["employee_id"].isin(existing_skus)]
            save_df_in_db(df, Employee._meta.db_table)
            # Remover el archivo
            # os.remove(full_path)

            return Response({"status": "Procesamiento exitoso"}, status=status.HTTP_200_OK)
        except Exception as e:
            # En caso de excepción, devolvemos un error
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
