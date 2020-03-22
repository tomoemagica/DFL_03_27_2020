@echo off
call _internal\setenv.bat
chdir /d "%WORKSPACE%\data_dst\aligned_debug"
echo please wait...
for %%F in (*.jpg) do call :sub "%%F"
pause
exit

:sub
set filename=%~n1
if not exist %WORKSPACE%\data_dst\aligned\%filename%*.jpg (del %WORKSPACE%\data_dst\aligned_debug\%filename%*.* echo %1)
goto :eof