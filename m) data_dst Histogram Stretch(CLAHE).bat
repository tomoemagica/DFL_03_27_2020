@echo off
call _internal\setenv.bat

mkdir "%WORKSPACE%\data_dst" 2>nul

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed extract-video ^
    --input-file "%WORKSPACE%\data_dst.*" ^
    --output-dir "%WORKSPACE%\data_dst" ^
    --fps 0

py "%INTERNAL%\faceutil\clahe.py"

ffprobe -i %WORKSPACE%\data_dst.mp4 2>&1 | grep bitrate | gawk -F: '{print $6}' | gawk -F' ' '{print $1}' > tmp.txt

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "%WORKSPACE%\data_dst\clahe" ^
    --output-file "%WORKSPACE%\clahe.mp4" ^
    --reference-file "%WORKSPACE%\data_dst.*" ^
    --include-audio < tmp.txt

del tmp.txt

pause