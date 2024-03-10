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

nlp = English()
sentencizer = Sentencizer()
np.set_printoptions(precision=2)


with open("Isaac.txt", "r") as isaacF:
    isaacLines = [line.strip() for line in isaacF.readlines()]
    print(f"isaac len: {len(isaacLines)}")

with open("SAP.txt", "r") as sapF:
    sapLines = [line.strip() for line in sapF.readlines()]
    print(f"sap len: {len(sapLines)}")

with open("ReactCourt.txt", "r") as reactF:
    reactLines = [line.strip() for line in reactF.readlines()]
    print(f"react len: {len(reactLines)}")

# isaacLines = isaacLines[0:10000]
# sapLines = sapLines[0:10000]
# reactLines = reactLines[0:10000]

labels = np.concatenate([
    np.repeat(np.array([1,0,0]).reshape((1,3)), len(isaacLines), axis=0), 
    np.repeat(np.array([0,1,0]).reshape((1,3)), len(sapLines), axis=0),
    np.repeat(np.array([0,0,1]).reshape((1,3)), len(reactLines), axis=0),
])

allLines = isaacLines + sapLines + reactLines

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