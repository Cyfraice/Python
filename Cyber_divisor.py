from moviepy.editor import *

a=input("Inserisci il titolo del video: ")

video_path = a+".mp4"

video = VideoFileClip(video_path)

audio = video.audio

b=input("Inserisci il titolo del file audio: ")

audio_path =b+".mp3"
audio.write_audiofile(audio_path)

video.close()
audio.close()

print("File audio creato!")
print("Puoi usare lo sbobinatore.")

c = input("Premi un tasto per chiudere il programma.")