@echo off
REM 【必須】NETを呼び出すライブラリ
::call conda install -c conda-forge pythonnet --yes
call py -3.7 -m pip install pythonnet
echo;