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
from keras.layers import TimeDistributed
from keras.layers import Bidirectional
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold



#################################################
## Data Loading and Preprocessing for Training ##
#################################################

df=pd.read_csv("R10.csv")
train=df[df.op!=131]
test=df[df.op==131]
corpus_train=train.chord.values
total_words = len(corpus_train) + 1
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus_train)
total_words = len(tokenizer.word_index) + 1
input_sequences_train = []
token_list_train = tokenizer.texts_to_sequences(corpus_train)
token_list_train = list(itertools.chain(*token_list_train))
for i in range(1, len(token_list_train)):
    n_gram_sequence_train = token_list_train[i:i+10]
    input_sequences_train.append(n_gram_sequence_train)
max_sequence_len = max([len(x) for x in input_sequences_train])
input_sequences_train = np.array(pad_sequences(input_sequences_train, maxlen=10, padding='pre'))
predictors_train, label_train = input_sequences_train[:,:-1],input_sequences_train[:,-1]
label_train=np_utils.to_categorical(label_train)
new_input_train=np.reshape(input_sequences_train,(input_sequences_train.shape[0],input_sequences_train.shape[1],1))
new_pred_train=np.reshape(predictors_train,(predictors_train.shape[0],predictors_train.shape[1],1))


######################
## Cross Validation ##
######################

kfold = KFold(n_splits=5, shuffle=True, random_state=18)
cvscores = []
for train, test in kfold.split(new_pred_train, label_train):
  model = Sequential()
  model.add(LSTM(256, return_sequences=True, input_shape=(new_pred_train.shape[1],1)))
  model.add(Dropout(0.5))
  model.add(Bidirectional(LSTM(128, return_sequences=True),input_shape=(9,1)))
  model.add(LSTM(64, return_sequences=False))
  model.add(Dropout(0.3))
  model.add(Dense(total_words,activation='softmax'))
  model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
  model.fit(new_pred_train[train], label_train[train], nb_epoch=25)
  scores = model.evaluate(new_pred_train[test], label_train[test], verbose=0)
  print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
  print(scores)
  cvscores.append(scores[1] * 100)
print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))
  

#############
## Testing ##
#############


