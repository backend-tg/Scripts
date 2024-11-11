import os

# Основной путь к директории, в которой будут сортироваться файлы
main_path = 'd:\\down'

# Словарь с категориями файлов: ключи — типы файлов, значения — списки расширений для каждого типа
extensions = {
    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv', 'rm', 'swf', 'vob'],
    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 'tar', 'xml'],
    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],
    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],
    'archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],
    'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],
    '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],
    'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],
    'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],
    'font': ['otf', 'ttf', 'fon', 'fnt'],
    'gif': ['gif'],
    'exe': ['exe'],
    'bat': ['bat'],
    'apk': ['apk']
}

# Функция создает папки для каждого типа файлов, если они еще не существуют
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        # Проверка, существует ли папка; если нет, создается
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')

# Функция возвращает список путей к подкаталогам в указанной директории
def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    return subfolder_paths

# Функция возвращает список путей к файлам в указанной директории
def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    return file_paths

# Функция сортирует файлы, перемещая их в соответствующие папки по расширениям
def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)  # Получаем список файлов в директории
    ext_list = list(extensions.items())       # Преобразуем словарь расширений в список пар (тип, расширения)

    for file_path in file_paths:
        extension = file_path.split('.')[-1]  # Извлекаем расширение файла
        file_name = file_path.split('\\')[-1] # Извлекаем имя файла

        # Ищем папку для данного расширения и перемещаем файл
        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')

# Функция удаляет пустые папки после сортировки файлов
def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        # Проверяем, пустая ли папка; если да, удаляем
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)

# Основная часть программы
if __name__ == "__main__":
    create_folders_from_list(main_path, extensions)  # Создаем папки для каждой категории файлов
    sort_files(main_path)                            # Сортируем файлы по папкам
    remove_empty_folders(main_path)                  # Удаляем пустые папки
