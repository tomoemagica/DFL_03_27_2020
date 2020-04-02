import sys
import os
from os import path
from pathlib import Path, PureWindowsPath
from shutil import move
import cv2

INTERNAL = os.environ['INTERNAL']
WORKSPACE = os.environ['WORKSPACE']

target_dir = WORKSPACE
target_dir = os.path.join(target_dir, 'data_src', 'aligned')

file_count = len(os.listdir(target_dir))

print("Checking " + str(file_count) + " files")

no_face_path = os.path.join(target_dir, 'no_face')

if not path.isdir(no_face_path):
    try:
        os.mkdir(no_face_path)
    except OSError:
        print("Creation of the directory %s failed" % no_face_path)
    else:
        print("Successfully created the directory %s " % no_face_path)

face_cascade = cv2.CascadeClassifier(INTERNAL + "/faceutil/haarcascade_frontalface_alt2.xml")
profile_cascade = cv2.CascadeClassifier(INTERNAL + "/faceutil/haarcascade_profileface.xml")

for thisFile in os.listdir(target_dir):
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):
        file_name = os.path.join(target_dir, thisFile)

        img_color = cv2.imread(file_name)
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            img_gray, scaleFactor=1.05, minNeighbors=3, minSize=(45, 45))

        profiles = profile_cascade.detectMultiScale(
            img_gray, scaleFactor=1.05, minNeighbors=3, minSize=(30, 30))

        if len(faces) == 0 and len(profiles) == 0:
            no_face_file = os.path.join(no_face_path, thisFile)
            if os.path.isfile(file_name):
                move(
                    file_name, no_face_file)
