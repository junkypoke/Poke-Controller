@echo off
REM ユーザー変数//////////////////////////////////////////////////////////////////////////
REM プロジェクト名
REM デフォルト値	:PokeCon3_6
REM 備考:0_CreatEnv.batにあるプロジェクト名と同じにすること
set ProjectName="PokeCon3_6"

REM activate.batの保存場所
REM デフォルト値:C:\Users\(user)\Anaconda3\Scripts\activate
REM Anacondaインストール先を変更していなければ変更不要
set batfile="%USERPROFILE%\Anaconda3\Scripts\activate.bat"

REM 以降ソース////////////////////////////////////////////////////////////////////////////

call %batfile%
call conda activate %ProjectName%

set cd_tmp=%~dp0
set cd_tmp2=%cd_tmp%SerialController
cd %cd_tmp2%
echo ソフトを起動します

REM Poke-Controller起動
python Window.py
pause
