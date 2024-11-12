import yt_dlp

ydl_opts = {"continuedl": True}
link = input("Добавьте ссылку на видео: ")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
