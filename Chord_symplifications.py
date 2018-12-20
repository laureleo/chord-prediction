##########################################################################
## Script to simplify chords and reduce the number of total classes 	##
## Fit some chords into higher category based on their harmonic features##
## Replace certain rare chords with value 'R'							##
## Output: a csv file with updated values								##
##########################################################################

import pandas as pd
import numpy as np
df=pd.read_csv('all_annotations.tsv', sep='\t')
freqs=df.chord.value_counts()
for i in range(0,df.shape[0]):
    if ("/" in df.chord[i] and (df.chord==df.chord[i]).sum()<100):
        df=df.replace(df.chord[i], df.chord[i].split("/", 1)[0])
        
for i in range(0,df.shape[0]):
    if ("(" in df.chord[i] and (df.chord==df.chord[i]).sum()<100):
        df=df.replace(df.chord[i], df.chord[i].split("(", 1)[0])
        
for i in range(0,df.shape[0]):
    if (df.chord[i][0]!="." and "." in df.chord[i] and (df.chord==df.chord[i]).sum()<100):
        df=df.replace(df.chord[i], df.chord[i].split(".", 1)[0])
        
for i in range(0,df.shape[0]):
    if ("[" in df.chord[i]):
        df=df.replace(df.chord[i], df.chord[i].split("[", 1)[0])
        
for i in range(0,df.shape[0]):
    if ("]" in df.chord[i]):
        df=df.replace(df.chord[i], df.chord[i].split("]", 1)[0])
        
for i in range(0,df.shape[0]):
    if (df.chord[i][0]=="." and (df.chord==df.chord[i]).sum()<50 and "." in df.chord[i][1:]):
        df=df.replace(df.chord[i],df.chord[i][:df.chord[i][1:].find(".")+1])

for i in range(0,df.shape[0]):
    if ((df.chord==df.chord[i]).sum()<10):
        df=df.replace(df.chord[i],'R')
        df=df.replace(df.figbass[i],np.NaN)
df.to_csv("R10.csv",index=False)


