from spacy.lang.en import English
from spacy.pipeline import Sentencizer
from keras.preprocessing.text import Tokenizer
from keras.layers import Input, Dense
from keras.models import Model
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