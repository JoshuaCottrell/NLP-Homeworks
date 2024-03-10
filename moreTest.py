from youtube_transcript_api import YouTubeTranscriptApi

#Look into how to import video id from playlist, that would make this sooo easy

# #Open File
# f = open("SAP.txt", "w+")

# #Create list of video id's (starts on "You gotta save to spend")
# sapid = [
#     "cKi0EeAoaHE",
#     "3UMYKGJwUqU",
#     "H6ckQ2HNiK8",
#     "59fLrYrSNwE",
#     "KM2nHRcuFhg",
#     "fkMCKWvZwZ0",
#     "cZNzwsVCMh0",
#     "RQn6lEN4X8I",
#     "PfvjrfLXwDw",
#     "pV6xMtp3O0o",
#     "tu5NhKQaClQ",
#     "6Kv83PFlJVc",
#     "W3q1nicbeAA",
#     "fwECE_koMs4",
#     "lHdqNm8D-Pw",
#     "-CCfTjL1umQ",
#     "eCMOAhHa8cE",
#     "u0FPn589W1w",
#     "utYRxrbBTz4",
#     "9phWh0TzwBM",
#     "Tx--cSzL-eM",
#     "VBZI0ODNjfA",
#     "k_xHiaDmRxs",
#     "czYS2mjRmVU",
#     "PXzho7a-P10",
#     "TCM3ilF6g-U",
#     "I45n13ldE0M",
#     "NoV6xa-uB4Q",
#     "zCtLA4z2jZs",
#     "vEyoOD_Wi1g",
#     "NISbNRj9RRg",
#     "y5mLz9qvOSs",
#     "YRvwk7NYFBY",
#     "km9ddJ4Dppk",
#     "13or2GtouXU",
#     "lymYvFLitbk",
#     "51nFPDdpYa8",
#     "jEqqjlei6Bw",
#     "E1whVAzCBDk",
#     "5G_M6ohZZY8",
#     "KkGoLzlx7uI",
#     "wETUDPCMys8",
#     "6cVOF8zk4Dc",
#     "Lq4Eyqqjguk",
#     "soc_vYp_N5A",
#     "tzjQ5jesnYg",
#     "XhQb2Ol7xZc",
#     "oB9g3pxobxU",
#     "m8Z7Nfu2vjE",
#     "XYuEpdr0kN4",
#     "3yeilxahGnk",
#     "KMBUZq8e35M",
#     "9ZiQSNj8hVA",
#     "gzALFAvxCUY",
#     "wJ7dU7D5S0w",
#     "u4bGP6-cg88",
#     "IWmNqg_Hujw",
#     "RNGILMn9WHo",
#     "orM2FMFW-yo",
#     "lReCgUAAI8k",
#     "fxLBJ16bkjk",
#     "oNacPFNIbRU",
#     "VSGEZgSQAeM",
#     "GaS6lF_mQSs",
#     "xVFGb2oKwws",
#     "CQVlVOjd_Mg",
#     "JvmBXuaoWnE",
#     "fRbHnSupmas",
#     "-BQAhwdEZ7s",
#     "HsQPDCwHAw8",
#     "VOKpnkvLJak",
#     "qprkcQUwZLU",
#     "9xS9YID1-i8",
#     "rKGqbfJV-QE",
#     "OMENDWDygHs",
#     "LJ4KxiqhqYw",
#     "7V20rUs67No",
#     "g53cn3asIXE",
#     "wMJDj22Xevo",
#     "UT5uUdvj86w",
#     "lk6KTL7HO_4",
#     "ogn-zQhOeVg",
#     "9dptehfpeVM",
#     "aaqfyiDbsSE",
#     "5svryghKJUo",
#     "1RJyAVdHXw0",
#     "MInwThz7r8I",
#     "Bl4xpw2FXcE",
#     "5TC3NJPjXRg",
#     "RWyaJnNbNpk"]

# print(len(sapid))

# #For every item in list
# for x in sapid:
#     #Get the transcript
#     srt = YouTubeTranscriptApi.get_transcript(x)
#     #For each item in the transcript
#     for i in srt:
#         #Ignore [Music]
#         if (i['text'] != "[Music]"):
#             #Write text to file
#             f.write("{}\n".format(i['text']))
#     #Triple new line after every video        
#     f.write("\n\n\n")

# f.close()

# #Open File
# f = open("ReactCourt.txt", "w+")

# #Create list of video id's (starts on "AITA for avoiding being murdered?")
# rcid = [
#     "Yjkvq3UB5pg",
#     "3PLWQBQeDpA",
#     "IxBwhGLox4o",
#     "rfwqLUArgvk",
#     "D6a1k0uaeJA",
#     "1gNJIQn7C1c",
#     "AIjkndSayiA",
#     "SPLyWZALP50",
#     "D5XFriladgs",
#     "rjM1XsmwE1M",
#     "ceyQSdRdci8",
#     "Wkfpmrpbq1o",
#     "M5xTe43v7LY",
#     "pQ2D4qTB9b0",
#     "Kc_9egTICOI",
#     "jStRXTxXthQ",
#     "0LnES9Wl3lE",
#     "1798Cztd0N8",
#     "8PfDUEGNAl4",
#     "bzSOPtG-1HU",
#     "EB1f8kELpoM",
#     "UOUPDkXlD0w",
#     "mBHIgKBy-QY",
#     "Ji4BHiX0WPg",
#     "03kp1svslaU",
#     "799UABajfYE",
#     "7I8qCmLF_6I",
#     "KsrMNOFwhus",
#     "N4WuzRSC3xM",
#     "8U0wzCF6fkw",
#     "FBaG7MO1oAk",
#     "UAC8g-It28U",
#     "bFXeQL_Hmjo",
#     "YARjYS25URs",
#     "H6K4PbqEJRE",
#     "GKhVVUSL8Eo",
#     "tAiFK0HySL4",
#     "XDXDUNBHXtE",
#     "qT7P-uxV9ho",
#     "zPrmpMxNI0g",
#     "53O9RKlYcA4",
#     "XbMfESX3c3o",
#     "KaeBMqi06kQ",
#     "2H3OHls_ReQ",
#     "IkQBovX13UQ",
#     "IkJFPGLBnY4",
#     "GDVEHPUvrq0",
#     "DtWi08xBEtQ",
#     "019hwCsZ9kM",
#     "jWHbuE3URXw",
#     "g23Jo_mG1jg",
#     "YzElwBgy6Lw",
#     "bEXJFaQnJ8M",
#     "IJt3FoJnu6Q"]

# #For every item in list
# for x in rcid:
#     #Get the transcript
#     srt = YouTubeTranscriptApi.get_transcript(x)
#     #For each item in the transcript
#     for i in srt:
#         #Ignore [Music]
#         if (i['text'] != "[Music]"):
#             #Write text to file
#             f.write("{}\n".format(i['text']))
#     #Triple new line after every video
#     f.write("\n\n\n")

# f.close()

#Open File
f = open("Isaac.txt", "w+")

#Create list of video id's (starts on "This one hurt")
isacid = [
"9_4oRrj-JXE",
"KbE4WNefBpU",
"AlvusfyAKzA",
"kvREbohKioQ",
"NW4baOlxhS4",
"rgJb3LGJm_g",
"qRKbyyhpJXs",
"VnCqz9UVFzM",
"EXoiYq-dOrY",
"DfIjAwxpPBo",
"VMX2wnU0-tg",
"KTOt3Z17KEY",
"ZiYx4uKTRrE",
"_i-MFfbi3LE",
"l6AQN0EDyRg",
"xW-gYMVMvak",
"rLjvFy-4K00",
"8Vzt0W3qKnI",
"SeFG2suL3OU",
"r6XwLpSyCbI",
"-jJIC9o7NvU",
"g_6GK83TGCo",
"PbBTAGg7OuI",
"yJgEq_MVOoc",
"YZvw4_j8pbw",
"9s40U3znys8",
"keV_LDavsbg",
"ruwmWUguzUI",
"7gh-7Tu1kX8",
"hr18_xdwQHo",
"2XMGfUATbMU",
"PPEX6j1Z9_A",
"TJIYYZLBJYs",
"UHKHb79FHqs",
"TzNTm703IEY",
"rmaZxGx75go",
"3U_nE7e-QeA",
"RYBiGVqmA44",
"KY-lIAhmXiw",
"mHjusbj4d_E",
"0WwNnei8b6A",
"KSoA60Qi7kQ",
"MWucYzYaQ8k",
"ge6mmDBNGHU",
"FAka1Vl6D5k",
"rG1lmlQydLI",
"uX3WDJOfy5I",
"wrU944B4SCw",
"1sCUQgEsoZE",
"SpdGjMSZ9dY",
"bToi99BIb3w",
"L8HKpQvVFJo",
"_1zFjwhs5GA",
"MevBR5Ol9sg",
"nlu7tLulqDg",
"6qvg5c1r2uA",
"_27GDvFfnHk",
"n7GeAT-CSMI",
"5tcO_ljtb6k",
"VRDwaQuQNL8",
"JHtKtEON2xI",
"rpmmOTNt8Xk",
"0Vb8oUWZiQ8",
"oozpLprXx6o",
"kpDoPNeJ1TI",
"seMAEqFwV-o",
"EbEJVyMYd7Q",
"WNL0p2OW0Yo",
"x6Bcxf47p6I",
"-bH1PZqjZaQ",
"6aG8TWlRXWs",
"9TFaXrcWaEg",
"8xDWGu41F9c",
"Ue2wGOmisfQ",
"Elk1bN4tjlY",
"gvPc3d8O09w",
"bvE5e4zq6J0",
"5_jwuq67b-M",
"fePVqHIWg4g",
"TGe2lTSV_VE",
"KfDcarEVn8k",
"PnDfaJVEEiU",
"0lkOndB2Dj0",
"C80sLRa2xhY",
"uJnOvRQnnsc",
"RwMpKMeHIA8",
"ThKH2TUr4Jc",
"hAHdnnX3l1A",
"euRQKNGq-gc",
"liXTxCX36lM"]

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
