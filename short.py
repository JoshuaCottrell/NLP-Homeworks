from youtube_transcript_api import YouTubeTranscriptApi

#Look into how to import video id from playlist, that would make this sooo easy

#Open File
f = open("SAP.txt", "w+")

#Create list of video id's (starts on "You gotta save to spend")
sapid = ["wTONiHZ8-Jo", "MmIjHnebGTQ", "_3PiZuuAnEw", "cKi0EeAoaHE", "3UMYKGJwUqU", "H6ckQ2HNiK8", "59fLrYrSNwE"]

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
rcid = ["Yjkvq3UB5pg", "3PLWQBQeDpA", "IxBwhGLox4o", "rfwqLUArgvk", "D6a1k0uaeJA"]

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
isacid = ["9_4oRrj-JXE", "KbE4WNefBpU", "AlvusfyAKzA", "kvREbohKioQ", "NW4baOlxhS4"]

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
