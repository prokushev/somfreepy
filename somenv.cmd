@echo off
rem $Id: somenv.cmd 2876 2012-09-08 23:12:15Z rogerb $

if "%SOMBASE%x" == "x" if exist "%ProgramFiles%\somtk" set SOMBASE=%ProgramFiles%\somtk
if "%SOMBASE%x" == "x" if exist "%ProgramFiles(x86)%\somtk" set SOMBASE=%ProgramFiles(x86)%\somtk

if "%SOMBASE%x" == "x" goto firsttime

set SOMIR=%SOMBASE%\etc\som.ir
set SOMENV=%SOMBASE%\etc\somenv.ini
set SC=%SOMBASE%\bin\sc.exe
set LIB=%SOMBASE%\lib;%LIB%
set INCLUDE=%SOMBASE%\include;%INCLUDE%
set PATH=%SOMBASE%\bin;%PATH%
py test.py
goto end

:firsttime
echo Edit %0 to set SOMBASE.

:end
