import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_sequences(train_x, train_y, seq_length):
    """
    Input:
        train_x, train_y: Features and their corresponding labels
        seq_length: the length of the sequences
    Return:
        lstm_x: a matrix where elements are on the form (sequence, sequence length, features)
        lstm_y: a matrix where elements are on the form (sequence, classes)
    Notes: 
        Does not generate sequences for the last (seq_length - 1) datapoints
        Takes quite a lot of computing with long sequence lengths.


    """
    #containers for the sequences we generate
    lstm_input = []
    lstm_output = []

    for i in range(0, train_x.shape[0] - (seq_length +1)):
        #Create a sequence
        in_data = train_x.iloc[i:seq_length + i].values
        lstm_input.append(in_data)

        #Select the chord that would have appeared after the sequence
        out_data = train_y.iloc[seq_length + i].values
        lstm_output.append(out_data) 

    #Convert to arrays
    lstm_x = np.array(lstm_input)
    lstm_y = np.array(lstm_output)

    return lstm_x, lstm_y

def remap(one_hot, columns):
    """
    Takes a one-hot encoded sequence of chords and converts them into the original chords
    """
    df = pd.DataFrame(one_hot, columns=columns)
    return df.idxmax(axis=1)
