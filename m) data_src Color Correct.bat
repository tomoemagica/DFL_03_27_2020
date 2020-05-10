@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" util ^
    --input-dir "%WORKSPACE%\data_src\aligned" ^
    --unpack-faceset

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" util ^
    --input-dir "%WORKSPACE%\data_src\aligned" ^
    --save-faceset-metadata

py "%INTERNAL%\faceutil\colcor.py"

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" util ^
    --input-dir "%WORKSPACE%\data_src\aligned" ^
    --restore-faceset-metadata

pause