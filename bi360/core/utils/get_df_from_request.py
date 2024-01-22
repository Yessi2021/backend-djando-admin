import os

import pandas as pd
from django.conf import settings


def get_df_from_request(data):
    # Extraemos la información necesaria de request.data
    mapping = data.get("mapping")
    file_path = data.get("path")
    sheet_name = data.get("sheetName")
    header_row = data.get("sheetIndex")

    base_dir = os.path.join(settings.MEDIA_ROOT, "temp_files")
    full_path = os.path.join(base_dir, file_path)

    # Verificamos si el archivo existe
    if not os.path.isfile(full_path):
        return None

    # Read file
    try:
        df = pd.read_excel(
            full_path,
            sheet_name=sheet_name,
            header=header_row,
            usecols=list(mapping.values()),
        )

        # Resetear los índices
        df.reset_index(drop=True, inplace=True)

        # Renombramos las columnas utilizando el mapeo proporcionado
        df.rename(columns={value: key for key, value in mapping.items()}, inplace=True)

        return df
    except Exception as e:
        print(e)
        return None
