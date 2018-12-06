from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.callbacks import EarlyStopping
from keras.models import Sequential
import keras.utils as ku 
import numpy as np 
import pandas as pd
import itertools
from keras.utils import np_utils
df=pd.read_csv("updated_chords.csv")
for i in range(0,df.shape[0]):
    if ((df.chord==df.chord[i]).sum()<10):
        df=df.replace(df.chord[i],'R')
        df=df.replace(df.figbass[i],np.NaN)
df=df[df.op==127]
corpus=df.chord.values
total_words = len(corpus) + 1
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1
input_sequences = []
token_list = tokenizer.texts_to_sequences(corpus)
token_list = list(itertools.chain(*token_list))
for i in range(1, len(token_list)):
    n_gram_sequence = token_list[:i+1]
    input_sequences.append(n_gram_sequence)
max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
label=np_utils.to_categorical(label)
new_input=np.reshape(input_sequences,(input_sequences.shape[0],input_sequences.shape[1],1))
new_pred=np.reshape(predictors,(predictors.shape[0],predictors.shape[1],1))
model = Sequential()
#model.add(Embedding(total_words, 10, input_shape=(input_sequences.shape[1],1))) #input_length=max_sequence_len-1))
model.add(LSTM(512, input_shape=(new_input.shape[0],1)))
model.add(Dropout(0.2))
#model.add(LSTM(100))
model.add(Dense(total_words,activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
earlystop = EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto')
model.fit(new_pred, label, nb_epoch=10, verbose=1,validation_split=0.2)#, callbacks=[earlystop])

print(model.summary())