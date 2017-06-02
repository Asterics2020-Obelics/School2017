# DetectingQuasars
A project to train machine learning algorithms to detect quasars using images from the <a href="http://www.sdss.org/">Sloan Digital Sky Survey</a>. This project was created for The Society of Physics Students at Northeastern State University and the Y0 Physics Seminar.

A description of the project can be found <a href="https://www.dplessas.com/new-blog/2017/5/17/catching-quasars-with-neural-nets">here</a>.

## Files
<a href="https://github.com/LocalSymmetry/DetectingQuasars/blob/master/Data%20Collection.ipynb">Data Collection.ipynb</a> - Gathering images from the Sloan Digital Sky Survey using <a href="http://simbad.u-strasbg.fr/simbad/">SIMBAD Astronomical Database</a> and the <a href="http://astrostatistics.psu.edu/datasets/SDSS_quasar.html">Penn State Center for Astrostatistics</a>.

<a href="https://github.com/LocalSymmetry/DetectingQuasars/blob/master/Model%20Training.ipynb">Model Training.ipynb</a> - Training of a Random Forest, Simple Convolutional Neural Network, and an Inception Neural Network classifier to detect quasars.

<a href="https://github.com/LocalSymmetry/DetectingQuasars/blob/master/QuasarClassifier.py">QuasarClassifier.py</a> - A functional version of the quasar classifier. Requires the Inception Model Checkpoint files.

<a href="https://github.com/LocalSymmetry/DetectingQuasars/blob/master/QuasarCandidatePredictions.ipynb">QuasarCandidatePredictions.ipynb</a> - Using the trained classification model to predict if quasar candidates are quasars.

<a href="https://github.com/LocalSymmetry/DetectingQuasars/blob/master/NonQuasarsData.csv">NonQuasarsData.csv</a> - 94670 randomly chosen non-quasar celestial objects in the range of the Sloan Digital Sky Survey. Constructed from the Data Collection notebook. 

<a href="https://github.com/LocalSymmetry/DetectingQuasars/blob/master/QuasarCandidatesData.csv">QuasarCandidatesData.csv</a> - 5418 quasar candidate objects in the range of the Sloan Digital Sky Survey. Constructed from the Data Collection notebook. 

<a href="https://github.com/LocalSymmetry/DetectingQuasars/blob/master/train_data.csv">train_data.csv</a> - The training images randomly chosen in the Model Training notebook. Contains a data frame of 98763 image filenames with quasar classification. 

<a href="https://github.com/LocalSymmetry/DetectingQuasars/blob/master/valid_data.csv">valid_data.csv</a> - The validation images randomly chosen in the Model Training notebook. Contains a data frame of 21163 image filenames with quasar classification

<a href="https://github.com/LocalSymmetry/DetectingQuasars/blob/master/test_data.csv">test_data.csv</a> - The training images randomly chosen in the Model Training notebook. Contains a data frame of 21164 image filenames with quasar classification

<a href="https://github.com/LocalSymmetry/DetectingQuasars/blob/master/QuasarCandidateDataWithClassification.csv">QuasarCandidateDataWithClassification.csv</a> - 5418 quasar candidate objects in the range of the Sloan Digital Sky Survey and their classification probabilities by the trained model. 

<a href="https://www.dropbox.com/sh/abig8qytnqrnsth/AAAUjNOwqA0M1S2EBzc7DURfa?dl=0">Images and Inception Model Checkpoint</a> - Externally hosted on <a href="https://www.dropbox.com/">Dropbox</a> due to size. Contains the images from the Data Collection notebook and the parameters for the trained Inception ConvNet.

