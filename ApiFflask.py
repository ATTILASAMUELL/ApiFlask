import os
import pytube as pt
import moviepy.editor as mp
from flask import Flask, request
import re
import shutil

app = Flask('Youtube')

@app.route("/olaMundo", methods=["GET"])
def olamundo():
    return{"ola": "mundo"}

@app.route("/baixar/video", methods=["POST"])
def baixarConverte():

    #baixa
    url = str(request.get_json("url"))
    stream = pt.YouTube(url = url).streams.get_audio_only()
    stream.download('mp4')
    title = str(stream.title)
    stream.t

    #converte

    converter =  mp.AudioFileClip('mp4\\' + title + '.mp4')
    converter.write_audiofile('mp3\\' + title + '.mp3')

    return "baixou e converteu"
app.run()