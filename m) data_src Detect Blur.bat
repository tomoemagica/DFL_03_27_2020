@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%INTERNAL%\faceutil\blur_image.py" -t 11.0

pause