import sys
import os
from os import path
from pathlib import Path, PureWindowsPath
from shutil import move
import cv2
import fnmatch

INTERNAL = os.environ['INTERNAL']
WORKSPACE = os.environ['WORKSPACE']

target_dir = WORKSPACE
target_dir = os.path.join(target_dir, 'data_src', 'aligned')

file_count = len(fnmatch.filter(os.listdir(target_dir), "*.jpg"))

print("Checking " + str(file_count) + " files")

profile_path = os.path.join(target_dir, 'profile')

if not path.isdir(profile_path):
    try:
        os.mkdir(profile_path)
    except OSError:
        print("Creation of the directory %s failed" % profile_path)
    else:
        print("Successfully created the directory %s " % profile_path)

face_cascade = cv2.CascadeClassifier(INTERNAL + "/faceutil/haarcascade_profileface.xml")

Iter = 0

print("Extracting...")

for thisFile in os.listdir(target_dir):
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):
        file_name = os.path.join(target_dir, thisFile)

        img_color = cv2.imread(file_name)
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            img_gray, scaleFactor=1.05, minNeighbors=3, minSize=(30, 30))

        Iter += 1
        print("\r" + str(Iter) + '/' + str(file_count), end='')

        if len(faces) > 0:
            profile_file = os.path.join(profile_path, thisFile)
            if os.path.isfile(file_name):
                move(
                    file_name, profile_file)

print("\nDone.")
