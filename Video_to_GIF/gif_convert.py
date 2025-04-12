import os
from moviepy import VideoFileClip

def convert_video_to_gif(video_path: str, gif_path: str, start_time: float = 0, duration: float | None = None, fps: int = 10) -> None:
    """
    Конвертирует видео в GIF.
    
    :param video_path: Путь к исходному видеофайлу.
    :param gif_path: Путь для сохранения GIF.
    :param start_time: Начальный момент обрезки (секунды).
    :param duration: Длительность GIF (по умолчанию полное видео).
    :param fps: Частота кадров GIF.
    """
    try:
        if not os.path.exists(video_path):
            print(f"❌ Файл '{video_path}' не найден.")
            return
        
        video_clip = VideoFileClip(video_path)
        
        if duration:
            video_clip = video_clip.subclip(start_time, start_time + duration)

        video_clip.write_gif(gif_path, fps=fps)

        print(f"✅ GIF успешно сохранён: {gif_path}")

    except Exception as e:
        print(f"⚠️ Ошибка при конвертации: {e}")

if __name__ == "__main__":
    # Укажите путь к видеофайлу и выходному GIF
    input_video = "example.mp4"
    output_gif = "output.gif"

    # Конвертация видео в GIF (с возможностью обрезки)
    convert_video_to_gif(input_video, output_gif, start_time=2, duration=5, fps=15)
