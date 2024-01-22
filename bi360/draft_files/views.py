# from bi360.authentication.utils.permission import HasGroupPermission
import json

import pandas as pd
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bi360.business.models import UserBusinessRelationship
from bi360.core.utils.save_file import save_file


# Create your views here.
# Create your views here.
class CheckExcel(APIView):
    parser_classes = [MultiPartParser]

    permission_classes = [IsAuthenticated]

    # required_permissions = ["change_user"]

    def post(self, request):
        try:
            file_obj = request.FILES["file"]
            if not file_obj.name.lower().endswith(".xlsx"):
                return Response({"Formato de archivo no válido"}, status=status.HTTP_400_BAD_REQUEST)

            # Valid max size
            max_file_size_bytes = 500  # 500 MB
            if file_obj.size > (max_file_size_bytes * 1024 * 1024):
                return Response(
                    "El archivo pesa " + f"{round((file_obj.size / (1024 * 1024)),1)}MB" + ". El máximo permitido es" +
                    f" {max_file_size_bytes}MB",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Abre el archivo Excel
            excel_file = pd.ExcelFile(file_obj)

            sheets_info = {}
            for sheet_name in excel_file.sheet_names:
                df = excel_file.parse(sheet_name, nrows=8, header=None)
                df_json = df.to_json(orient="values")

                # Almacena el JSON resultante en sheets_info[sheet_name]
                sheets_info[sheet_name] = json.loads(df_json)

            business = UserBusinessRelationship.objects.filter(user=request.user).first().business
            owner = f"{request.user.first_name}"
            # owner = f"sales/{request.user.first_name}"
            save_file(file_obj, f"{file_obj.name.lower()}", f"{business.name}/{owner}")
            return Response(
                {
                    "sheets_info": sheets_info,
                    "path": f"{business.name}/{owner}/{file_obj.name.lower()}",
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
