import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

# Путь к папке с фотографиями
source_folder = "/path/to/photos"
destination_folder = "/path/to/sorted_photos"

# Получение даты съёмки из метаданных или даты создания файла


def get_date(photo_path):
    try:
        # Пытаемся получить дату из EXIF
        image = Image.open(photo_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                if TAGS.get(tag) == "DateTimeOriginal":
                    return value.split(" ")[0].replace(":", "-")
    except Exception as e:
        print(f"Ошибка чтения EXIF для {photo_path}: {e}")

    # Если EXIF недоступен, используем дату создания файла
    try:
        creation_time = os.path.getctime(photo_path)
        return datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d")
    except Exception as e:
        print(f"Ошибка получения даты создания для {photo_path}: {e}")
        return "unknown"

# Сортировка фотографий


def sort_photos():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Проверяем, является ли файл изображением
        if os.path.isfile(file_path) and filename.lower().endswith((".jpg", ".jpeg", ".png")):
            date_folder_name = get_date(file_path)

            # Создаём папку по дате
            date_folder = os.path.join(destination_folder, date_folder_name)
            os.makedirs(date_folder, exist_ok=True)

            # Перемещаем файл
            shutil.move(file_path, os.path.join(date_folder, filename))
            print(f"{filename} → {date_folder}")


# Запускаем сортировку
sort_photos()
