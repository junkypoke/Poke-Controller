@echo off
REM ユーザー変数//////////////////////////////////////////////////////////////////////////
REM プロジェクト名
REM デフォルト値	:PokeCon3_7
set ProjectName="PokeCon3_7"

REM activate.batの保存場所
REM デフォルト値:C:\Users\(user)\Anaconda3\Scripts\activate.bat
REM Anacondaインストール先を変更していなければ変更不要
set batfile="%USERPROFILE%\Anaconda3\Scripts\activate.bat"

REM 以降ソース////////////////////////////////////////////////////////////////////////////
REM カレントディレクトリをbatファイルのあるフォルダに設定
cd %~dp0

call %batfile%
call conda create -n %ProjectName% python=3.7 --yes

call conda activate %ProjectName%

REM インストール用のbatファイルが入っているフォルダ(すべてのバージョン)
set batf=%~dp0install_bat\ALL

for /r %batf% %%f in (*.bat) do (
    echo filename = %%f
    call %%f
)

REM インストール用のbatファイルが入っているフォルダ(Python3.7)
set batf=%~dp0install_bat\Python3.7

for /r %batf% %%f in (*.bat) do (
    echo filename = %%f
    call %%f
)

echo インストールの一連の処理を実行しました

pause