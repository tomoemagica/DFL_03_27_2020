# DFL_03_15_2020
 DFL_03_15_2020

8) merged to mp4.bat

To read the bit rate automatically from data_dst.mp4,

Requires grep and gawk.

These can be used by installing msys64, for example.

If you don't have grep and gawk, delete the following line:

ffprobe -i% WORKSPACE% \ data_dst.mp4 2> & 1 | grep bitrate | gawk -F: '{print $ 6}' | gawk -F '' '{print $ 1}'> tmp.txt

del tmp.txt

Change the following line

Before change: -include-audio <tmp.txt

Change: -include-audio

If you do not have grep and gawk, use VideoEd.py, which is not customized.

VideoEd.py

You can create videos in H.265 by changing libx264 to libx265.
