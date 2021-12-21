import subprocess
import os

os.chdir('/')


#give random subtitles to BBB 1 min video
subprocess.call(
   ['ffmpeg','-i','home/fran/Documents/container.mp4','-vf','subtitles=home/fran/Documents/subs.srt',
    '/home/fran/Documents/subbed_video.mp4'
])

