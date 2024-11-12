import moviepy.editor

video = moviepy.editor.VideoFileClip("video.mp4")

audio = video.audio

name = 'audio.mp3'
audio.write_audiofile(name)
