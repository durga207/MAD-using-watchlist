# Face morphing attack detection and attacker identification based on a watchlist

## face_similarity.py
This script compares a given image with a set of images in a directory to find the most similar face. It uses the face_recognition library to encode and compare faces. If a face in the directory is similar enough to the given image, the script outputs the percentage of similarity and displays the face image. If there is no similar face, the script outputs a message.


## requirements.txt
1. Dlib :- installation instruction in https://pysource.com/2019/03/20/how-to-install-dlib-for-python-3-on-windows/
2. face_recognition
3. pillow
4. pathlib

Execute by running python face_similarity.py command

