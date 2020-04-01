@echo off
call _internal\setenv.bat

mkdir "%WORKSPACE%\data_dst" 2>nul

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed extract-video ^
    --input-file "%WORKSPACE%\data_dst.*" ^
    --output-dir "%WORKSPACE%\data_dst" ^
    --output-ext "png" ^
    --fps 0

mkdir "%WORKSPACE%\data_dst_waifu" 2>nul

echo execute waifu2x-caffe-cui...

"C:\Program Files\waifu2x-caffe\waifu2x-caffe-cui.exe" -t 1 --gpu 0 -b 4 -p cudnn -h 1080 -i "%WORKSPACE%\data_dst" -o "%WORKSPACE%\data_dst_waifu"

ffprobe -i %WORKSPACE%\data_dst.mp4 2>&1 | grep bitrate | gawk -F: '{print $6}' | gawk -F' ' '{print $1}' > tmp.txt

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "%WORKSPACE%\data_dst_waifu" ^
    --output-file "%WORKSPACE%\waifu.mp4" ^
    --reference-file "%WORKSPACE%\data_dst.*" ^
    --include-audio < tmp.txt

del tmp.txt

pause