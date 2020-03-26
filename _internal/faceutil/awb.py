import cv2
import numpy as np
import os
import sys
from os import path
from pathlib import Path, PureWindowsPath

# Usage: py awb.py

def white_balance(img):
    result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
    return result

INTERNAL = os.environ['INTERNAL']
WORKSPACE = os.environ['WORKSPACE']

target_dir = WORKSPACE
target_dir = os.path.join(target_dir, 'data_dst')

file_count = len(os.listdir(target_dir))

print("Checking " + str(file_count) + " files")

awb_path = os.path.join(target_dir, 'awb')

if not path.isdir(awb_path):
    try:
        os.mkdir(awb_path)
    except OSError:
        print("Creation of the directory %s failed" % awb_path)
    else:
        print("Successfully created the directory %s " % awb_path)

for thisFile in os.listdir(target_dir):
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):
        img = cv2.imread(file_name)
        final = np.array(white_balance(img))
        basename = os.path.basename(file_name)
        cv2.imwrite(awb_path +  '/' + basename, final)
