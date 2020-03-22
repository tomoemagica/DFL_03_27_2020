@echo off
call _internal\setenv.bat

python -m labelme "%WORKSPACE%\data_dst\aligned"\ --autosave 
