# Face morphing attack detection and attacker identification based on a watchlist

## Dataset
1. civilian directory : 69 neutral frontal face images
2. watchlist directory : 102 neutral frontal face images
3. smiling_front-watchlist directory : 102 smiling frontal face images
4. neutral_left_3quarter direcroty : 102 neutral left angle face images
5. neutral_right_3quarter direcroty : 102 neutral right angle face images
6. spliced (,_50,_70,_90) : 102 neutral frontal face images generated by morphing faces from watchlist with the most similar face from he civilian list by using splicing technique with 100, 50, 70, 90 JPEG Quality Factor
7. retouched (,_50,_70,_90) : 102 neutral frontal face images generated by morphing faces from watchlist with the most similar face from he civilian list by using retouching technique with 100, 50, 70, 90 JPEG Quality Factor
8. complete (,_50,_70,_90) : 102 neutral frontal face images generated by morphing faces from watchlist with the most similar face from he civilian list by using complete technique with 100, 50, 70, 90 JPEG Quality Factor
9. combined (,_50,_70,_90) : 102 neutral frontal face images generated by morphing faces from watchlist with the most similar face from he civilian list by using combined techniquewith 100, 50, 70, 90 JPEG Quality Factor

## face_similarity.py
This script compares a given image with a set of images in a directory to find the most similar face. It uses the face_recognition library to encode and compare faces. If a face in the directory is similar enough to the given image, the script outputs the percentage of similarity and displays the face image. If there is no similar face, the script outputs a message.


## requirements.txt
1. Dlib :- installation instruction in https://pysource.com/2019/03/20/how-to-install-dlib-for-python-3-on-windows/
2. face_recognition
3. pillow
4. pathlib

Execute by running python face_similarity.py command

