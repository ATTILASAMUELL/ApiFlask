import os, sys
import pytube as pt
from pathlib import Path
import moviepy.editor as mp



url = "https://www.youtube.com/watch?v=XS088Opj9o0&list=RDXS088Opj9o0&start_radio=1"
stream = pt.YouTube(url = url).streams.get_audio_only()
stream.download('mp4')

title = str(stream.title)


some_path = 'C:/Users/Windows10/Desktop/python_flask/mp4/'+ title + '.mp4'


p = Path(some_path)
target = Path('C:/Users/Windows10/Desktop/python_flask/mp4/madonah.mp4')
p.rename(target)


#converte

converter =  mp.AudioFileClip('mp4/madonah.mp4')
converter.write_audiofile('mp3\\' + 'madonah' + '.mp3')

if os.path.exists("C:/Users/Windows10/Desktop/python_flask/mp4/madonah.mp4"):
  os.remove("C:/Users/Windows10/Desktop/python_flask/mp4/madonah.mp4")
