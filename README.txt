Final Project

THIS PROGRAM RUNS ON PYTHON AND REQUIRES THE OPENCV AND OPENCV-CONTRIB LIBRARIES

***************************************
TO RUN THE PROGRAM
From the SRC folder, type the following:

python project.py

****************************************

There are two parts to the project:
1. Image Encryption technique
2. Fingerprint encryption/decryption from dataset

For part 1:
_________________________________________________________
Encryption:
you will be prompted to enter a filename for an image

*******
These images can be found in the DATA/pictures folder
*******

Next, the program will prompt you to enter values for t and n.
The program works best when t=3.  When t=4, it sometimes works but not always.
Anything greater than 4 will result in the program terminating.


The program will then display the image in grayscale and prompt you to press enter.
The program will encrypt the images and save them in the DATA/pictures folder.

Decryption:

you will then be prompted to enter the exact filename of one of the shares and then its corresponding share value
enter these until you have entered at least t shares
press 'r' and the picture will be restored

For part 2:
_____________________________________________________________
part 2 will choose an image from the dataset at random and display it's feature points.
The program will then create a text file of the locations of the keypoints (titled answerkey) and .tsv files that contain the share values of the keypoints.
By pressing enter (after the first 3 images appear), the program will randomly decrypt 3 "shares" files and create a text file of the decrypted shares.  
