import cv2
import numpy as np
from shutil import move
import os
from os import path
import sys
from pathlib import Path, PureWindowsPath


INTERNAL = os.environ['INTERNAL']
WORKSPACE = os.environ['WORKSPACE']

target_dir = WORKSPACE
target_dir = os.path.join(target_dir, 'data_dst')

file_count = len(os.listdir(target_dir))

print("Checking " + str(file_count) + " files")

const_path = os.path.join(target_dir, 'const')

if not path.isdir(const_path):
    try:
        os.mkdir(const_path)
    except OSError:
        print("Creation of the directory %s failed" % const_path)
    else:
        print("Successfully created the directory %s " % const_path)


for thisFile in os.listdir(target_dir):
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):
        file_name = os.path.join(target_dir, thisFile)

        img = cv2.imread(file_name, cv2.IMREAD_COLOR)

        # normalize float versions
        norm_img = cv2.normalize(img, None, alpha=0, beta=1.2, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

        # scale to uint8
        norm_img = np.clip(norm_img, 0, 1)
        norm_img = (255*norm_img).astype(np.uint8)

        basename = os.path.basename(file_name)

        # write normalized output images
        cv2.imwrite(const_path +  '/' + basename, norm_img)

