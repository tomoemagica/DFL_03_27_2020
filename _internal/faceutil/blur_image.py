import argparse
import cv2
import os
from shutil import move
from os import path
import sys
from pathlib import Path, PureWindowsPath


ap = argparse.ArgumentParser()
ap.add_argument("-t", "--threshold", type=float, default=11.0,
                help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())


def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F)


INTERNAL = os.environ['INTERNAL']
WORKSPACE = os.environ['WORKSPACE']

target_dir = WORKSPACE
target_dir = os.path.join(target_dir, 'data_src', 'aligned')

blur_path = os.path.join(target_dir, 'blur')
not_blur_path = os.path.join(target_dir, 'not_blur')

if not path.isdir(blur_path):
    try:
        os.mkdir(blur_path)
    except OSError:
        print("Creation of the directory %s failed" % blur_path)
    else:
        print("Successfully created the directory %s " % blur_path)

if not path.isdir(not_blur_path):
    try:
        os.mkdir(not_blur_path)
    except OSError:
        print("Creation of the directory %s failed" % not_blur_path)
    else:
        print("Successfully created the directory %s " % not_blur_path)


for image_path in os.listdir(target_dir):
    file_name = os.path.join(target_dir, image_path)
    if os.path.isfile(file_name):
        file_name = os.path.join(target_dir, image_path)

        image = cv2.imread(file_name)
        image = cv2.resize(image, dsize=(256, 256))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        laplacian = variance_of_laplacian(gray)

        if laplacian.var() < args["threshold"]:
            move(
                file_name, blur_path)
        else:
            move(
                file_name, not_blur_path)
