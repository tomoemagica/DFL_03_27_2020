@echo off
call ..\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "%INTERNAL%\TecoGAN\output" ^
    --output-file "%INTERNAL%\TecoGAN\result.mp4" ^
    --reference-file "%WORKSPACE%\data_dst.*" ^
    --include-audio

pause