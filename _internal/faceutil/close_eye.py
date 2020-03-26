import dlib
import cv2
from shutil import move
import os
from os import path
import sys
from pathlib import Path, PureWindowsPath

INTERNAL = os.environ['INTERNAL']
WORKSPACE = os.environ['WORKSPACE']

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(INTERNAL + "/faceutil/shape_predictor_68_face_landmarks.dat")


def get_center(gray_img):
    moments = cv2.moments(gray_img, False)
    try:
        return int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])
    except:
        return None


def is_close(y0, y1):
    if abs(y0 - y1) < 11:
        return True
    return False


def eye_point(img, parts, left=True):
    if left:
        eyes = [
                parts[36],
                min(parts[37], parts[38], key=lambda x: x.y),
                max(parts[40], parts[41], key=lambda x: x.y),
                parts[39],
                ]
    else:
        eyes = [
                parts[42],
                min(parts[43], parts[44], key=lambda x: x.y),
                max(parts[46], parts[47], key=lambda x: x.y),
                parts[45],
                ]
    org_x = eyes[0].x
    org_y = eyes[1].y
    if is_close(org_y, eyes[2].y):
        return True
    else:
        return False


target_dir = WORKSPACE
target_dir = os.path.join(target_dir, 'data_src', 'aligned')
match_path = os.path.join(target_dir, 'close_eye')

if not path.isdir(match_path):
   try:
       os.mkdir(match_path)
   except OSError:
       print("Creation of the directory %s failed" % match_path)
   else:
       print("Successfully created the directory %s " % match_path)

file_count = len(os.listdir(target_dir))

print("Checking " + str(file_count) + " files")

for thisFile in os.listdir(target_dir):
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):
        file_name = os.path.join(target_dir, thisFile)

        image = file_name
        frame = cv2.imread(image)

        dets = detector(frame[:, :, ::-1])
        len_dets = len(dets)

        if len_dets > 0:
            parts = predictor(frame, dets[0]).parts()

            is_close_left = eye_point(frame, parts)
            is_close_right = eye_point(frame, parts, False)

            if is_close_left and is_close_right:
                move(
                    file_name, match_path)
