##################################################
## Exploratory Data Analysis and Visualizations ##
##################################################


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()


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


#rare chords per opus
ops=np.sort(df.op.unique())
rares=np.zeros(len(ops))
for i in range(0,len(ops)):
  foo=df[df.op==ops[i]]
  rares[i]=len(foo[foo.chord=="R"])/len(foo)*100


objects = ('18', '59', '74', '95', '127', '130','131','132','135')
y_pos = np.arange(len(objects))
performance = rares
 
plt.bar(y_pos, performance, align='center')
plt.xticks(y_pos, objects)
plt.ylabel('Percentage of Rare Chords')
plt.xlabel('Opus')
plt.title('Rare Chord Proportion in Each Opus')
 
plt.show()
