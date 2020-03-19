@echo off
cd /D %~dp0
call setenv.bat
cd %DFL_ROOT%
rmdir DFLIMG\__pycache__ /s /q
rmdir facelib\__pycache__ /s /q
rmdir localization\__pycache__ /s /q
rmdir mainscripts\__pycache__ /s /q
rmdir merger\__pycache__ /s /q
rmdir models\__pycache__ /s /q
rmdir samplelib\__pycache__ /s /q