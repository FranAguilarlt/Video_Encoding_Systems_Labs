import subprocess
import os

os.chdir('/')

# ask seconds of cropage
d = str(10)

subprocess.call(
    ['ffmpeg', '-ss', '00:00:00', '-i', 'home/fran/Documents/test.mp4', '-to', '00:00:' + d, '-c', 'copy',
     'home/fran/Documents/output.mp4'])

subprocess.call(
    ['ffmpeg','-y','-i','home/fran/Documents/output.mp4','-vf', 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay',
     'home/fran/Documents/histo.mp4'])

subprocess.call(
    ['ffmpeg','-i','home/fran/Documents/output.mp4','-vf', 'scale=1280:720',
     'home/fran/Documents/1280x720.mp4'])
subprocess.call(
    ['ffmpeg','-i','home/fran/Documents/output.mp4','-vf', 'scale=640:480',
     'home/fran/Documents/640x480.mp4'])
subprocess.call(
    ['ffmpeg','-i','home/fran/Documents/output.mp4','-vf', 'scale=320:240',
     'home/fran/Documents/320x240.mp4'])

subprocess.call(
    ['ffmpeg','-i','home/fran/Documents/output.mp4','-vf', 'scale=160:120',
     'home/fran/Documents/160x120.mp4'])

subprocess.call(
    ['ffmpeg','-i','home/fran/Documents/bagpipes.flac','-ac' ,'1',
     'home/fran/Documents/mono.mp3'])




