@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%INTERNAL%\faceutil\no_eye.py"

pause