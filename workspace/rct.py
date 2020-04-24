# USAGE
# py rct.py 00000.jpg etc

# import the necessary packages
from color_transfer import color_transfer
import numpy as np
import cv2
from shutil import move
import os
from os import path
import sys
from pathlib import Path, PureWindowsPath
import fnmatch


# load the images
source = sys.argv[1]
if not path.isfile(source):
    print("ERROR: File " + str(source) + " isn't valid")
    exit()

source = cv2.imread(source)

target_dir = os.getcwd()
target_dir = os.path.join(target_dir, 'data_dst')

if not path.isdir(target_dir):
    print("ERROR: Path " + str(target_dir) + " isn't a valid directory")
    exit()

file_count = len(fnmatch.filter(os.listdir(target_dir), "*.png"))

print("Checking " + str(file_count) + " files")

rct_path = os.path.join(target_dir, 'rct')

if not path.isdir(rct_path):
    try:
        os.mkdir(rct_path)
    except OSError:
        print("Creation of the directory %s failed" % rct_path)
    else:
        print("Successfully created the directory %s " % rct_path)

Iter = 0

print("Executing...")

for thisFile in os.listdir(target_dir):
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):
        file_name = os.path.join(target_dir, thisFile)

        Iter += 1
        print("\r" + str(Iter) + '/' + str(file_count), end='')

        target = cv2.imread(file_name)

        # transfer the color distribution from the source image
        # to the target image
        transfer = color_transfer(source, target, clip=True, preserve_paper=True)

        # check to see if the output image should be saved
        basename = os.path.basename(file_name)
        abs_filename = rct_path +  '/' + basename
        cv2.imwrite(abs_filename, transfer)

print("\nDone.")
