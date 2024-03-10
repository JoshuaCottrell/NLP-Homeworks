import spacy
nlp = spacy.load("en_core_web_sm")
import random
import sys

print(len(sys.argv))
if (3 >= len(sys.argv) >= 2):
    try:
        f = open(sys.argv[1], "r")
    except:
        print("File Not Found. Please try again")
        quit()
    n = 2 #default n
    if (len(sys.argv) == 3):
        try:
            n = int(sys.argv[2])
        except:
            print("Error: N is a non-integer. Please try again")
            quit()
        if (n > 100):
            print("Error: N is too large. Please try again")
            quit()


    ndict = dict()
    ngram = []
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        doc = nlp(line)
        for token in doc:
            if len(ngram) < n-1:
                ngram.append(token.lemma_)
                continue
            elif len(ngram) < n:
                ngram.append(token.lemma_)
                ng = ' '.join(ngram)
            else:
                ngram[0] = token.lemma_
                ngram = ngram[1:] + ngram[:1]
                ng = ' '.join(ngram)
            if ng in ndict:
                ndict[ng] += 1
            else:
                ndict[ng] = 1
    
    randomList = random.choices(list(ndict.keys()), weights=list(ndict.values()), k=int(100/n))

    print(f"{n}-gram sentence:\n")
    print(' '.join(randomList))

else:
    #Open SAP for reading
    f = open("SAP.txt", "r")
    
    unidict = dict()
    lines = f.readlines()
    
    #Unigram
    for line in lines:
        line = line.strip("\n")
        doc = nlp(line)
        for token in doc:
            if token.lemma_ in unidict:
                unidict[token.lemma_] += 1
            else:
                unidict[token.lemma_] = 1
    
    
    randomList = random.choices(list(unidict.keys()), weights=list(unidict.values()), k=100)
    
    print("Unigram sentence: \n")
    print(' '.join(randomList))
    
    #Bigram
    bidict = dict()
    bigram = []
    for line in lines:
        line = line.strip("\n")
        doc = nlp(line)
        for token in doc:
            if len(bigram) < 1:
                bigram.append(token.lemma_)
                continue
            elif len(bigram) < 2:
                bigram.append(token.lemma_)
                bg = ' '.join(bigram)
            else:
                bigram[0] = bigram[1]
                bigram[1] = token.lemma_
                bg = ' '.join(bigram)
            if bg in bidict:
                bidict[bg] += 1
            else:
                bidict[bg] = 1

    randomList = random.choices(list(bidict.keys()), weights=list(bidict.values()), k=50)

    print("\nBigram sentence: \n")
    print(' '.join(randomList))

    #Trigram
    tridict = dict()
    trigram = []
    for line in lines:
        line = line.strip("\n")
        doc = nlp(line)
        for token in doc:
            if len(trigram) < 2:
                trigram.append(token.lemma_)
                continue
            elif len(trigram) < 3:
                trigram.append(token.lemma_)
                tg = ' '.join(trigram)
            else:
                trigram[0] = trigram[1]
                trigram[1] = trigram[2]
                trigram[2] = token.lemma_
                tg = ' '.join(trigram)
            if tg in tridict:
                tridict[tg] += 1
            else:
                tridict[tg] = 1
    
    randomList = random.choices(list(tridict.keys()), weights=list(tridict.values()), k=33)
    
    print("\nTrigram sentence: \n")
    print(' '.join(randomList))









