from __future__ import division
import numpy as np
from colorcorrect.algorithm import white_balance, clahe
from shutil import move
import os
from os import path
import sys
from pathlib import Path, PureWindowsPath
import fnmatch
import cv2

'''
INTERNAL = os.environ['INTERNAL']
WORKSPACE = os.environ['WORKSPACE']
'''

target_dir = os.getcwd()
target_dir = os.path.join(target_dir, 'data_dst')

file_count = len(fnmatch.filter(os.listdir(target_dir), "*.png"))

print("Checking " + str(file_count) + " files")

colcor_path = os.path.join(target_dir, 'colcor')

if not path.isdir(colcor_path):
   try:
       os.mkdir(colcor_path)
   except OSError:
       print("Creation of the directory %s failed" % colcor_path)
   else:
       print("Successfully created the directory %s " % colcor_path)

Iter = 0

print("Executing...")


for thisFile in os.listdir(target_dir):
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):
        file_name = os.path.join(target_dir, thisFile)

        Iter += 1
        print("\r" + str(Iter) + '/' + str(file_count), end='')

        img = cv2.imread(file_name)

        img = white_balance(img)
        img = clahe(img)

        basename = os.path.basename(file_name)
        abs_filename = colcor_path +  '/' + basename
        cv2.imwrite(abs_filename, img)

print("\nDone.")

