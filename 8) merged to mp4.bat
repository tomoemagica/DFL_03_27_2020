@echo off
call _internal\setenv.bat

ffprobe -i %WORKSPACE%\data_dst.mp4 2>&1 | grep bitrate | gawk -F: '{print $6}' | gawk -F' ' '{print $1}' > tmp.txt

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "%WORKSPACE%\data_dst\merged" ^
    --output-file "%WORKSPACE%\result.mp4" ^
    --reference-file "%WORKSPACE%\data_dst.*" ^
    --include-audio < tmp.txt

del tmp.txt

pause