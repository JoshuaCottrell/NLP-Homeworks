from youtube_transcript_api import YouTubeTranscriptApi

#Look into how to import video id from playlist, that would make this sooo easy

#Open File
f = open("SAP.txt", "w+")

#Create list of video id's (starts on "You gotta save to spend")
sapid = ["wTONiHZ8-Jo", "MmIjHnebGTQ", "_3PiZuuAnEw", "cKi0EeAoaHE", "3UMYKGJwUqU", "H6ckQ2HNiK8", "59fLrYrSNwE", "KM2nHRcuFhg", "fkMCKWvZwZ0", "cZNzwsVCMh0", "cZNzwsVCMh0", "PfvjrfLXwDw", "pV6xMtp3O0o", "tu5NhKQaClQ", "6Kv83PFlJVc", "W3q1nicbeAA", "fwECE_koMs4", "lHdqNm8D-Pw", "-CCfTjL1umQ", "eCMOAhHa8cE"] 

#For every item in list
for x in sapid:
    #Get the transcript
    srt = YouTubeTranscriptApi.get_transcript(x)
    #For each item in the transcript
    for i in srt:
        #Ignore [Music]
        if (i['text'] != "[Music]"):
            #Write text to file
            f.write("{}\n".format(i['text']))
    #Triple new line after every video        
    f.write("\n\n\n")

f.close()

#Open File
f = open("ReactCourt.txt", "w+")

#Create list of video id's (starts on "AITA for avoiding being murdered?")
rcid = ["Yjkvq3UB5pg", "3PLWQBQeDpA", "IxBwhGLox4o", "rfwqLUArgvk", "D6a1k0uaeJA", "1gNJIQn7C1c", "AIjkndSayiA", "SPLyWZALP50", "D5XFriladgs", "rjM1XsmwE1M", "ceyQSdRdci8", "Wkfpmrpbq1o", "M5xTe43v7LY", "pQ2D4qTB9b0", "Kc_9egTICOI", "jStRXTxXthQ", "0LnES9Wl3lE", "1798Cztd0N8", "8PfDUEGNAl4", "bzSOPtG-1HU"]

#For every item in list
for x in rcid:
    #Get the transcript
    srt = YouTubeTranscriptApi.get_transcript(x)
    #For each item in the transcript
    for i in srt:
        #Ignore [Music]
        if (i['text'] != "[Music]"):
            #Write text to file
            f.write("{}\n".format(i['text']))
    #Triple new line after every video
    f.write("\n\n\n")

f.close()

#Open File
f = open("Isaac.txt", "w+")

#Create list of video id's (starts on "This one hurt")
isacid = ["9_4oRrj-JXE", "KbE4WNefBpU", "AlvusfyAKzA", "kvREbohKioQ", "NW4baOlxhS4", "rgJb3LGJm_g", "qRKbyyhpJXs", "VnCqz9UVFzM", "EXoiYq-dOrY", "DfIjAwxpPBo", "VMX2wnU0-tg", "KTOt3Z17KEY", "ZiYx4uKTRrE", "_i-MFfbi3LE", "l6AQN0EDyRg", "xW-gYMVMvak", "rLjvFy-4K00", "8Vzt0W3qKnI", "SeFG2suL3OU", "r6XwLpSyCbI"]

#For every item in list
for x in isacid:
    #Get the transcript
    srt = YouTubeTranscriptApi.get_transcript(x)
    #For each item in the transcript
    for i in srt:
        #Ignore [Music]
        if (i['text'] != "[Music]"):
            #Write text to file
            f.write("{}\n".format(i['text']))
    #Triple new line after every video
    f.write("\n\n\n")

f.close()
