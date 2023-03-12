import face_recognition
from pathlib import Path
from PIL import Image
import sys

img1_path = sys.argv[1] + ".png"
img2_path = "compare/" + sys.argv[2] + ".png"

    
known_image = face_recognition.load_image_file(img1_path)
known_image_encoding = face_recognition.face_encodings(known_image)[0]
unknown_image = face_recognition.load_image_file(img2_path)
face_encodings = face_recognition.face_encodings(unknown_image)
face_distance = face_recognition.face_distance(face_encodings, known_image_encoding)[0]
similarity = (1 - face_distance)* 100
sim = round(similarity,2)
print("Similarity between 2 images is ",sim,"%")

