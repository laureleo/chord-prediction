
# chord-prediction

This project focuses on deep learning approaches for chord prediction in Ludwig van Beethoven's string quartets given a progression of its preceding chords. Recurrent neural networks (RNN) were used to design predictive models. In particular, N-gram-based approach was used to train long short-term memory (LSTM) and bidirectional LSTM network models on a dataset of Beethoven's quartets' harmonic analyses. 


## Run
Make sure all the requirements are fulfilled. 
Then enter jupyter and run the notebook 'run.ipynb'
## Folder structure

* **visualizations.py**
Generation of chord distributions and other plots

* **chord_functions.py**
Convenience functions, for generating sequences for example

* **run.ipynb**
Notebook to run to produce final results

* **cross_fold_weights/best/**
Contains the weights from after the training process used for the final result

* **data/**
Contains the original and modified data files with the annotated chords

## Requirements:
* pandas==0.23.0
* seaborn==0.9.0
* matplotlib==2.2.2
* scikit-learn==0.19.1
* scipy==1.1.0
* numpy==1.14.3
