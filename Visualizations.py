##################################################
## Exploratory Data Analysis and Visualizations ##
##################################################


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


#original data
df0=pd.read_csv('all_annotations.tsv', sep='\t')
freqs0=df0.chord.value_counts()
plt.hist(freqs0,bins=100)
plt.yscale('log')
plt.title('Distribution of Original Chord Occurences')
plt.xlabel('Number of Occurences')
plt.ylabel('Frequencies log-scaled')

#updated data
df=pd.read_csv('R10.csv')
freqs=df.chord.value_counts()
plt.hist(freqs)
plt.yscale('log')
plt.title("Distribution of Chord Occurences After Preprocessing")
plt.xlabel("Number of Occurences")
plt.ylabel('Frequencies log-scaled')


