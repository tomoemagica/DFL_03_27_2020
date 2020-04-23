from __future__ import division
import numpy as np
from six.moves import range
from six.moves import xrange
from PIL import Image
from shutil import move
import os
from os import path
import sys
from pathlib import Path, PureWindowsPath
import fnmatch

def stretch_pre(nimg):
    """
    from 'Applicability Of White-Balancing Algorithms to Restoring Faded Colour Slides: An Empirical Evaluation'
    """
    nimg = nimg.transpose(2, 0, 1)
    nimg[0] = np.maximum(nimg[0] - nimg[0].min(), 0)
    nimg[1] = np.maximum(nimg[1] - nimg[1].min(), 0)
    nimg[2] = np.maximum(nimg[2] - nimg[2].min(), 0)
    return nimg.transpose(1, 2, 0)


def gray_world(nimg):
    nimg = nimg.transpose(2, 0, 1).astype(np.uint32)
    mu_g = np.average(nimg[1])
    nimg[0] = np.minimum(nimg[0] * (mu_g / np.average(nimg[0])), 255)
    nimg[2] = np.minimum(nimg[2] * (mu_g / np.average(nimg[2])), 255)
    return nimg.transpose(1, 2, 0).astype(np.uint8)


def max_white(nimg):
    if nimg.dtype == np.uint8:
        brightest = float(2 ** 8)
    elif nimg.dtype == np.uint16:
        brightest = float(2 ** 16)
    elif nimg.dtype == np.uint32:
        brightest = float(2 ** 32)
    else:
        brightest = float(2 ** 8)
    nimg = nimg.transpose(2, 0, 1)
    nimg = nimg.astype(np.int32)
    nimg[0] = np.minimum(nimg[0] * (brightest / float(nimg[0].max())), 255)
    nimg[1] = np.minimum(nimg[1] * (brightest / float(nimg[1].max())), 255)
    nimg[2] = np.minimum(nimg[2] * (brightest / float(nimg[2].max())), 255)
    return nimg.transpose(1, 2, 0).astype(np.uint8)


def stretch(nimg):
    return max_white(stretch_pre(nimg))


def from_pil(pimg):
    pimg = pimg.convert(mode='RGB')
    nimg = np.array(pimg)
    return nimg


def to_pil(nimg):
    return Image.fromarray(np.uint8(nimg))


INTERNAL = os.environ['INTERNAL']
WORKSPACE = os.environ['WORKSPACE']

target_dir = WORKSPACE
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

        img = Image.open(file_name)
        img = to_pil(stretch(gray_world(from_pil(img))))
        basename = os.path.basename(file_name)
        abs_filename = colcor_path +  '/' + basename
        img.save(abs_filename)

print("\nDone.")
