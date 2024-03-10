import spacy
import numpy as np
import math
nlp = spacy.load("en_core_web_sm")


print("Loading corpora (be patient)...\n\n")

#Get word count for SAP corpus
fSAP = open("SAP.txt", "r") #Open file
wcountSAP = dict() #New dict for word count
lines = fSAP.readlines() #Get lines
numLinesSAP = len(lines) #Get number of lines for percentage
count = 0 #Count for percentage
percent = 0 #Percent for percentage
wordsSAP = 0 #Tracks total word count
for line in lines: # For every line in the file
    line = line.strip("\n") #Get rid of any newlines
    doc = nlp(line) #Parse with spacy
    wordsSAP += len(doc) #each token is a word so add words in this line to word count
    for token in doc: #For each token in this line
        if token.lemma_ in wcountSAP: #If it is already in the dictionary add 1 to its count
            wcountSAP[token.lemma_] += 1
        else: #Otherwise add it to the dictionary (with laplace smoothing applied)
            wcountSAP[token.lemma_] = 2
    count += 1 #Increase line tracker
    last = math.trunc(percent) #Get last percent so I don't spam percents all the time
    percent = (count/numLinesSAP) * 50 #Get current percent max 50% since this is 1 of 2 corpora
    if (math.trunc(percent) % 10 == 0 and math.trunc(percent) != last): #Print in intervals of 10%
        print(f"{math.trunc(percent)}%")
        
            

#Get word count for ReactCourt corpus
fReact = open("ReactCourt.txt", "r") #Everything is the same as above but for react court document
wcountReact = dict() 
lines = fReact.readlines()
numLinesReact = len(lines)
count = 0
percent = 50
wordsReact = 0
for line in lines:
    line = line.strip("\n")
    doc = nlp(line)
    wordsReact += len(doc)
    for token in doc:
        if token.lemma_ in wcountReact:
            wcountReact[token.lemma_] += 1
        else:
            wcountReact[token.lemma_] = 2
    count += 1
    last = math.trunc(percent)
    percent = ((count/numLinesReact) * 50) + 50
    if (math.trunc(percent) % 10 == 0 and math.trunc(percent) != last):
        print(f"{math.trunc(percent)}%")


#Laplce smoothing for words that are in the corpus but not in one file or the other.
#If one dictionary has a word that is not in the other dictionary, add it with a value of 1
print("\nPerforming laplace smoothing...\n")

plus1React = 0
for word in wcountSAP:
    if word not in wcountReact:
        wcountReact[word] = 1
        plus1React += 1

plus1SAP = 0
for word in wcountReact:
    if word not in wcountSAP:
        wcountSAP[word] = 1
        plus1SAP += 1

divSAP = plus1SAP + wordsSAP
divReact = plus1React + wordsReact

print("Done!\n")


#Start actual program loop
phrase = ""
while (phrase.lower() != "q"):

    #Keep track of last phrase for diagnostics
    lastPhrase = phrase
    
    #Get user input
    print("Enter a phrase (q to quit): ")
    phrase = input()
    
    #Check for quit input
    if (phrase.lower() == "q"):
        print("\nBye!")
        break;

    #Diagnostics mode
    if (phrase.lower() == "d"):
        print(f"\n\nLast phrase: {lastPhrase}")
        print(f"Tokens and word counts:")
        print(f"{'Token' : <10}{'WC SAP' : ^10}{'WC React' : >10}")
        for token in doc:
            print(f"{token.lemma_ : <10}{phraseDictSAP[token.lemma_] : ^10}{phraseDictReact[token.lemma_] : >10}")
        print(f"Probability SAP: {probabilitySAP}")
        print(f"Probability React: {probabilityReact}")
        continue;

    #Reset variables
    phraseDictSAP = dict()
    phraseDictReact = dict()
    probabilitySAP = 0
    probabilityReact = 0

    #Parse with spacy
    doc = nlp(phrase)
    
    #Words from phrase that are in SAP corpus
    for token in doc:
        if token.lemma_ in wcountSAP:
            phraseDictSAP[token.lemma_] = wcountSAP[token.lemma_]
        elif token.lemma_ in wcountReact:
            phraseDictSAP[token.lemma_] = 1
        else:
            phraseDictSAP[token.lemma_] = 0
                
    #Words from phrase that are in React corpus
    for token in doc:
        if token.lemma_ in wcountReact:
            phraseDictReact[token.lemma_] = wcountReact[token.lemma_]
        elif token.lemma_ in wcountSAP:
            phraseDictReact[token.lemma_] = 1
        else:
            phraseDictReact[token.lemma_] = 0

    #Get log probabilities for both corpora
    for value in phraseDictSAP.values():
        value = value / divSAP
        if value == 0:
            continue
        probabilitySAP += np.log(value)

    for value in phraseDictReact.values():
        value = value / divReact
        if value == 0:
            continue
        probabilityReact += np.log(value)

    #If probabilities of both are 0 then no words are in the corpora
    if probabilitySAP == 0 and probabilityReact == 0:
        print("No words given are in corpora\n")
        continue

    #Un-log probabilities, normalize (maybe not right word), and convert to percentages
    probabilitySAP = pow(10, probabilitySAP)
    probabilityReact = pow(10, probabilityReact)
    tot = probabilitySAP + probabilityReact
    probabilitySAP = (probabilitySAP / tot) * 100
    probabilityReact = (probabilityReact / tot) * 100

    #Print greater of the two probabilities
    if probabilitySAP > probabilityReact:
        print("Prediction: SAP")
        print(f"Confidence: {probabilitySAP}\n")
    else:
        print("Prediction: React")
        print(f"Confidence: {probabilityReact}\n")







#Can keep as it but look at book and actual smoothing and try to incorporate that but more importantly understand it





    

    
                

        
