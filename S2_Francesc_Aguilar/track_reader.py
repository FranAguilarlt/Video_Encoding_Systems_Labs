import re, subprocess
import broadcast_std_checker


#t = ['v','a']

#check video codec names
v = subprocess.check_output(
    ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=codec_name', '-of',
     'default=noprint_wrappers=1:nokey=1',
     '/home/fran/Documents/container.mp4'],encoding='UTF-8')

audios = []
for i in range(2) : #for every audio stream check codec name
    o = str(i)
    a = subprocess.check_output( ['ffprobe','-v', 'error' ,'-select_streams' ,'a:'+o ,'-show_entries' ,'stream=codec_name','-of','default=noprint_wrappers=1:nokey=1',
    '/home/fran/Documents/container.mp4'],encoding='UTF-8')
    audios.append(a.strip())


broadcast_std_checker.BroadcastStandard_Checker(v,audios)