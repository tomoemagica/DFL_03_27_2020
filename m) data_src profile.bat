@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%INTERNAL%\faceutil\profile.py"

pause