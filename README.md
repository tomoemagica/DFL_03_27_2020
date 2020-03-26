# DFL_03_25_2020
 DFL_03_25_2020

## 8) merged to mp4.bat

8) merged to mp4.bat

To read the bit rate automatically from data_dst.mp4,

Requires grep and gawk.

These can be used by installing msys64, for example.

If you don't have grep and gawk, delete the following line:

ffprobe -i% WORKSPACE%\data_dst.mp4 2> & 1 | grep bitrate | gawk -F: '{print $ 6}' | gawk -F '' '{print $ 1}'> tmp.txt

del tmp.txt

Change the following line

Before change: -include-audio <tmp.txt

Change: -include-audio


## VideoEd.py

If you do not have grep and gawk, use VideoEd.py, which is not customized.

VideoEd.py

You can create videos in H.265 by changing libx264 to libx265.


## ModelBase.py  io.input_skip_pending ()

During the first train,

[0] 0 is automatically input before Autobackup every N hour (0..24?: Help) is input.

This is probably a bug.

For the second and subsequent trains, you can enter Autobackup every N hour.

ModelBase.py

After commenting out io.input_skip_pending (), you will be able to input.

\# io.input_skip_pending ()

No side effects.


# m) data_src close eye.bat

## Preparation

Install python

Install dlib

## download

http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

Decompress with WinRar etc.

Unzip the shape_predictor_68_face_landmarks.dat file

Put it under _internal\faceutil\

## how to use

m) data_src close eye.bat

## function

In the face image under\workspace\data_src\aligned, the face with closed eyes

Move to workspace\data_src\aligned\close_eye folder.


# m) data_dst Auto White Balance.bat
# m) data_dst Contrast Stretch.bat
# m) data_dst Histogram Stretch(CLAHE).bat

## Preparation

To read the bit rate automatically from data_dst.mp4,

Requires grep and gawk.

These can be used by installing msys64, for example.

## how to use

m) data_dst Auto White Balance.bat

m) data_dst Contrast Stretch.bat

m) data_dst Histogram Stretch(CLAHE).bat


## function

Automatically white balance video of data_dst.mp4.

Stretch the contrast of the video of data_dst.mp4.

Stretch the brightness of the video of data_dst.mp4.
