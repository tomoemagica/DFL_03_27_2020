import face_recognition
from shutil import move
import os
from os import path
import sys
from pathlib import Path, PureWindowsPath

# Usage: py match_frame.py data_src\00000.png etc.

# Set up commmand line args
file_to_recognize = sys.argv[1]
target_dir = os.getcwd()
target_dir = os.path.join(target_dir, 'data_src')


if not path.isfile(file_to_recognize):
    print("ERROR: File " + str(file_to_recognize) + " isn't valid")
    exit()

if not path.isdir(target_dir):
    print("ERROR: Path " + str(target_dir) + " isn't a valid directory")
    exit()

file_count = len(os.listdir(target_dir))

print("Checking " + str(file_count) + " files")

match_path = os.path.join(target_dir, 'match')

if not path.isdir(match_path):
    try:
        os.mkdir(match_path)
    except OSError:
        print("Creation of the directory %s failed" % match_path)
    else:
        print("Successfully created the directory %s " % match_path)


if os.path.isfile(file_to_recognize):
    picture_of_me = face_recognition.load_image_file(file_to_recognize)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

for thisFile in os.listdir(target_dir):
   
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):
        file_name = os.path.join(target_dir, thisFile)

        new_picture = face_recognition.load_image_file(file_name)

        for face_encoding in face_recognition.face_encodings(new_picture):

            results = face_recognition.compare_faces(
                [my_face_encoding], face_encoding, 0.5)

            if results[0] == True:
                match_file = os.path.join(match_path, thisFile)
                if os.path.isfile(file_name):
                    move(
                        file_name, match_file)
