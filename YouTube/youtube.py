import yt_dlp

try:
    # Ввод ссылки от пользователя
    link = input("Добавьте ссылку на видео: ").strip()
    if not link:
        raise ValueError("Ссылка не может быть пустой!")

    # Настройки загрузки
    ydl_opts = {
        "format": "best[ext=mp4]/best",  # Выбирает лучший формат с видео и аудио в одном файле
        "outtmpl": "%(title)s.%(ext)s",  # Шаблон имени файла
        "socket_timeout": 100,  # Увеличенное время ожидания соединения
        "retries": 5,  # Количество повторных попыток
        "noplaylist": True,  # Отключить загрузку плейлистов
    }

    # Загрузка видео
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

except ValueError as ve:
    print(f"Ошибка: {ve}")
except yt_dlp.utils.DownloadError as de:
    print(f"Ошибка загрузки: {de}")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
