@echo off
call ..\setenv.bat

mkdir output 2>nul

cd TGMAIN

echo;
tgmain.exe TG-STD
cd ..

pause
