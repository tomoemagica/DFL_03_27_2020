@echo off
call ..\setenv.bat

mkdir "%WORKSPACE%\data_dst" 2>nul

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed extract-video ^
    --input-file "%WORKSPACE%\data_dst.*" ^
    --output-dir "%INTERNAL%\TecoGAN\input" ^
    --output-ext "png" ^
    --fps 0

pause