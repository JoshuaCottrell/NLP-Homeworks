from spacy.lang.en import English
from spacy.pipeline import Sentencizer
from keras.preprocessing.text import Tokenizer
from keras.layers import Input, Dense, Embedding, Flatten
from keras.models import Model
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import re
import tensorflow as tf
import sys
import cv2

def defaultFiles(fns):
    with open("Isaac.txt", "r") as isaacF:
        isaacLines = [line.strip() for line in isaacF.readlines()]
        print(f"f1 len: {len(isaacLines)}")

    with open("SAP.txt", "r") as sapF:
        sapLines = [line.strip() for line in sapF.readlines()]
        print(f"f2 len: {len(sapLines)}")

    with open("ReactCourt.txt", "r") as reactF:
        reactLines = [line.strip() for line in reactF.readlines()]
        print(f"f3 len: {len(reactLines)}")

    # Just reading them in without this breaks it for some reason?... i'm not sure
    isaacLines = isaacLines[0:10000]
    sapLines = sapLines[0:10000]
    reactLines = reactLines[0:10000]

    return isaacLines, sapLines, reactLines

def intBow(fns, default):
    nlp = English()
    sentencizer = Sentencizer()
    np.set_printoptions(precision=2)
    
    if (default):
        f1Lines, f2Lines, f3Lines = defaultFiles(fns)
        minimum = 10000
    else:
        with open(fns[0], encoding="utf-8") as f1:
            f1Lines = [line.strip() for line in f1.readlines()]
            print(f"f1 len: {len(f1Lines)}")

        with open(fns[1], encoding="utf-8") as f2:
            f2Lines = [line.strip() for line in f2.readlines()]
            print(f"f2 len: {len(f2Lines)}")

        with open(fns[2], encoding="utf-8") as f3:
            f3Lines = [line.strip() for line in f3.readlines()]
            print(f"f3 len: {len(f3Lines)}")

        minimum = min(len(f1Lines), len(f2Lines), len(f3Lines))

    f1Lines = f1Lines[:minimum]
    f2Lines = f2Lines[:minimum]
    f3Lines = f3Lines[:minimum]

    labels = np.concatenate([
        np.repeat(np.array([1,0,0]).reshape((1,3)), len(f1Lines), axis=0), 
        np.repeat(np.array([0,1,0]).reshape((1,3)), len(f2Lines), axis=0),
        np.repeat(np.array([0,0,1]).reshape((1,3)), len(f3Lines), axis=0),
    ])

    allLines = f1Lines + f2Lines + f3Lines

    t = Tokenizer()
    t.fit_on_texts(allLines)
    dtm = t.texts_to_matrix(allLines, mode="tfidf")

    input_layer = Input(shape=(dtm.shape[1],))
    hidden_layer = Dense(20, activation='relu')(input_layer)
    output_layer = Dense(3, activation='softmax')(hidden_layer)
    model = Model(inputs=input_layer, outputs=output_layer)
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(dtm, labels, epochs=20, verbose=0)

    sent = input("Enter a sentence (\"done\" to exit): ")
    while (sent != 'done'):
        coded = t.texts_to_matrix([sent], mode='tfidf')
        print(model.predict(coded))
        sent = input("Enter a sentence: ")
    return

def evalBow(fns, default):
    nlp = English()
    sentencizer = Sentencizer()
    np.set_printoptions(precision=2)

    if (default):
        f1Lines, f2Lines, f3Lines = defaultFiles(fns)
        minimum = 10000
    else:
        with open(fns[0], encoding="utf-8") as f1:
            f1Lines = [line.strip() for line in f1.readlines()]
            print(f"f1 len: {len(f1Lines)}")

        with open(fns[1], encoding="utf-8") as f2:
            f2Lines = [line.strip() for line in f2.readlines()]
            print(f"f2 len: {len(f2Lines)}")

        with open(fns[2], encoding="utf-8") as f3:
            f3Lines = [line.strip() for line in f3.readlines()]
            print(f"f3 len: {len(f3Lines)}")

        minimum = min(len(f1Lines), len(f2Lines), len(f3Lines))

    f1Lines = f1Lines[:minimum]
    f2Lines = f2Lines[:minimum]
    f3Lines = f3Lines[:minimum]

    labels = np.concatenate([
        np.repeat(np.array([1,0,0]).reshape((1,3)), len(f1Lines), axis=0), 
        np.repeat(np.array([0,1,0]).reshape((1,3)), len(f2Lines), axis=0),
        np.repeat(np.array([0,0,1]).reshape((1,3)), len(f3Lines), axis=0),
    ])

    allLines = f1Lines + f2Lines + f3Lines

    t = Tokenizer()
    t.fit_on_texts(allLines)

    def evaluate(input, gold, numTrials):
        dtm = t.texts_to_matrix(input, mode="tfidf")
        accuracies = np.empty(numTrials)
        for trial in range(numTrials):
            print(f"trial #{trial}...")
            Xtrain, Xtest, ytrain, ytest = train_test_split(dtm, gold, test_size=.2)
            input_layer = Input(shape=(dtm.shape[1],))
            hidden_layer = Dense(20, activation='relu')(input_layer)
            output_layer = Dense(3, activation='softmax')(hidden_layer)
            model = Model(inputs=input_layer, outputs=output_layer)
            model.compile(loss='categorical_crossentropy', metrics=['accuracy'])
            model.fit(Xtrain, ytrain, epochs=20, verbose=0)
            accuracies[trial] = model.evaluate(Xtest, ytest)[1]
        return accuracies


    accs = evaluate(allLines, labels, 20)
    mean = np.mean(accs)
    stdDevi = np.std(accs)
    print(f"Accuracies: {accs} \n Mean: {mean} \n Standard Deviation: {stdDevi} \n")
    return

def evalSeq(fns, default):
    nlp = English()
    sentencizer = Sentencizer()
    np.set_printoptions(precision=2)

    if (default):
        f1Lines, f2Lines, f3Lines = defaultFiles(fns)
        minimum = 10000
    else:
        with open(fns[0], encoding="utf-8") as f1:
            f1Lines = [line.strip() for line in f1.readlines()]
            print(f"f1 len: {len(f1Lines)}")

        with open(fns[1], encoding="utf-8") as f2:
            f2Lines = [line.strip() for line in f2.readlines()]
            print(f"f2 len: {len(f2Lines)}")

        with open(fns[2], encoding="utf-8") as f3:
            f3Lines = [line.strip() for line in f3.readlines()]
            print(f"f3 len: {len(f3Lines)}")

        minimum = min(len(f1Lines), len(f2Lines), len(f3Lines))

    f1Lines = f1Lines[:minimum]
    f2Lines = f2Lines[:minimum]
    f3Lines = f3Lines[:minimum]

    labels = np.concatenate([
        np.repeat(np.array([1,0,0]).reshape((1,3)), len(f1Lines), axis=0), 
        np.repeat(np.array([0,1,0]).reshape((1,3)), len(f2Lines), axis=0),
        np.repeat(np.array([0,0,1]).reshape((1,3)), len(f3Lines), axis=0),
    ])

    allLines = f1Lines + f2Lines + f3Lines
    t = Tokenizer()
    t.fit_on_texts(allLines)

    vocabSize = len(t.word_index) + 1
    E = np.zeros(shape=(vocabSize, 50))
    with open("glove.6B.50d.txt", encoding='utf-8') as f:
        for line in f:
            stuff = line.split()
            word = stuff[0]
            if word in t.word_index:
                # print(f"Yes! adding embedding for word {word} (at row {t.word_index[word]})")
                numbers = np.array([ float(x) for x in stuff[1:] ])
                E[t.word_index[word],:] = numbers


    def evaluate(input, gold, numTrials):
        encoded = t.texts_to_sequences(allLines)
        padded = pad_sequences(encoded, maxlen=10, padding="post")
        accuracies = np.empty(numTrials)
        for trial in range(numTrials):
            print(f"trial #{trial}...")
            Xtrain, Xtest, ytrain, ytest = train_test_split(padded, gold, test_size=.2)
            input_layer = Input(shape=(padded.shape[1],))
            e_layer = Embedding(vocabSize, 50, input_length=10, weights=[E], trainable=False)(input_layer)
            f_layer = Flatten()(e_layer)
            hidden_layer = Dense(20, activation='relu')(f_layer)
            output_layer = Dense(3, activation='softmax')(hidden_layer)
            model = Model(inputs=input_layer, outputs=output_layer)
            model.compile(loss='categorical_crossentropy', metrics=['accuracy'])
            model.fit(Xtrain, ytrain, epochs=20, verbose=0)
            accuracies[trial] = model.evaluate(Xtest, ytest)[1]
        return accuracies


    accs = evaluate(allLines, labels, 20)
    mean = np.mean(accs)
    stdDevi = np.std(accs)
    print(f"Accuracies: {accs} \n Mean: {mean} \n Standard Deviation: {stdDevi} \n")
    return


fns = []
if (len(sys.argv) == 4):
    fns.append(sys.argv[1])
    fns.append(sys.argv[2])
    fns.append(sys.argv[3])
    print("Corpora loaded")
    default = False
else:
    print("Enter corpora file names (remember to include .txt!)")
    print("(I can't promise this will work for corpora that aren't mine) (enter \"default\" for my corpora)")
    fns.append(input(""))
    if (fns[0] == "default"):
        fns[0] = "Isaac.txt"
        fns.append("SAP.txt")
        fns.append("ReactCourt.txt")
        default = True
    else:
        fns.append(input(""))
        fns.append(input(""))
        default = False

print("Welcome to homework 4!")
print("Corpora:")
for i in range(len(fns)):
        print(f"File{i}: {fns[i]}")
print("What would you like to do?")
print("1. Interactive BOW")
print("2. Evaluate BOW")
print("3. Evaluate SEQ")
print("4. Change Corpora")
print("5. Exit Program")
choice = input("")
while (choice != "5"):
    if (choice == "1"):
        intBow(fns, default)
    elif (choice == "2"):
        evalBow(fns, default)
    elif (choice == "3"):
        evalSeq(fns, default)
    elif (choice == "4"):
        print("Enter corpora file names (remember to include .txt!)")
        print("(I can't promise this will work for corpora that aren't mine) (enter \"default\" for my corpora)")
        fns[0] = input("")
        if (fns[0] == "defualt"):
            fns[0] = "Isaac.txt"
            fns[1] = "SAP.txt"
            fns[2] = "ReactCourt.txt"
            default = True
        else:
            fns[1] = input("")
            fns[2] = input("")
            default = False

    print("Corpora:")
    for i in range(len(fns)):
        print(f"File{i}: {fns[i]}")
    print("What would you like to do?")
    print("1. Interactive BOW")
    print("2. Evaluate BOW")
    print("3. Evaluate SEQ")
    print("4. Change Corpora")
    print("5. Exit Program")
    choice = input("")

print("Thanks for grading my homework!")
##windowName = "Press Q to exit"
##video = cv2.VideoCapture("video.mp4")
##cv2.namedWindow(windowName)
##while (True):
##    ret, frame = video.read()
##    if not ret:
##        print("broke")
##        cv2.destroyWindow(windowName)
##        break
##    cv2.imshow(windowName, frame)
##
##    waitKey = (cv2.waitKey(1) & 0xFF)
##    if  waitKey == ord('q'): #if Q pressed you could do something else with other keypress
##         print("closing video and exiting")
##         cv2.destroyWindow(windowName)
##         video.release()
##         break
