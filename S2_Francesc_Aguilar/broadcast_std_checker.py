def BroadcastStandard_Checker(Video,Audio):

    h264 = False
    MPEG2 = False
    AC3 = False
    AAC = False
    MP3 = False


    if("h264" in Video):
        h264=True
    if("mp2" in Video):
        MPEG2 = True
    if("ac3" in Audio):
        AC3 = True
    if("aac" in Audio):
        AAC = True
    if ("mp3" in Audio):
        MP3 = True

    if((h264 or MPEG2) and (AC3 or AAC or MP3)):
        print("\n The file can be broadcasted in DVB Standard\n")
    if ((h264 or MPEG2) and (AAC)):
        print("\n The file can be broadcasted in ISDB Standard\n")
    if ((h264 or MPEG2) and (AC3)):
        print("\n The file can be broadcasted in ATSC Standard\n")

    else :
        print("Error no matching broadcast stadndard")
