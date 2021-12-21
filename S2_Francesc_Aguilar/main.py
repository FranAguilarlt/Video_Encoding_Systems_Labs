
import subprocess
import os

os.chdir('/')

#cut the video for d seconds
subprocess.call(
    ['ffmpeg', '-ss', '00:00:00', '-i', 'home/fran/Documents/BBB.mp4', '-to', '00:01:00' , '-c', 'copy',
     'home/fran/Documents/s2_BBB.mp4'])

#Obtaining the mp3 file
subprocess.call(
   ['ffmpeg','-i', 'home/fran/Documents/s2_BBB.mp4',
     'home/fran/Documents/s2_audio_BBB.mp3'])

#Obtaining the aac file
subprocess.call(
   ['ffmpeg','-i', 'home/fran/Documents/s2_BBB.mp4','-c:a','aac','-q:a','2',
     'home/fran/Documents/s2_aac_BBB.m4a'])

#Packing everything in a mp4 container
subprocess.call(
     ['ffmpeg','-i', 'home/fran/Documents/s2_BBB.mp4',
      '-i','home/fran/Documents/s2_audio_BBB.mp3',
      '-i','home/fran/Documents/s2_aac_BBB.m4a','-map','0','-map', '0:0','-map','1:0','-c','copy','-shortest',
      'home/fran/Documents/container.mp4'])

