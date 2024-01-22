import os

from django.conf import settings


def save_file(file, name, app_name):
    app_media_root = os.path.join(settings.MEDIA_ROOT, f"temp_files/{app_name}")
    os.makedirs(app_media_root, exist_ok=True)

    file_path = os.path.join(app_media_root, name)

    with open(file_path, "wb") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
