import spacy
import math

nlp = spacy.load("en_core_web_sm")


print("Loading corpora (be patient)...\n\n")
        

#Get word count for ReactCourt corpus
fReact = open("ReactCourt.txt", "r") #Stolen code from my hw3
wcountReact = dict() 
lines = fReact.readlines()
numLinesReact = len(lines)
count = 0
percent = 0
wordsReact = 0
for line in lines:
    line = line.strip("\n")
    doc = nlp(line)
    wordsReact += len(doc)
    for entity in doc.ents:
        if entity.text in wcountReact:
            wcountReact[entity.text][1] += 1
        else:
             wcountReact[entity.text] = [entity.label_, 1]
    count += 1
    last = math.trunc(percent)
    percent = ((count/numLinesReact) * 100)
    if (math.trunc(percent) % 10 == 0 and math.trunc(percent) != last):
        print(f"{math.trunc(percent)}%")


print("Done!\n")
ner = ["PERSON", "LOC", "ORG"]
with open("test.txt", "w") as f:
    for key in wcountReact:
        if wcountReact[key][1] > 5:
            print(f"{key}", file=f)

    for key in wcountReact:
        if wcountReact[key][1] > 5:
            print(f"{wcountReact[key][0]}", file=f)

    for key in wcountReact:
        if wcountReact[key][1] > 5:
            print(f"{wcountReact[key][1]}", file=f)









