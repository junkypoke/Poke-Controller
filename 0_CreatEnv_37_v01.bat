@echo off
REM ���[�U�[�ϐ�//////////////////////////////////////////////////////////////////////////
REM �v���W�F�N�g��
REM �f�t�H���g�l	:PokeCon3_7
set ProjectName="PokeCon3_7"

REM activate.bat�̕ۑ��ꏊ
REM �f�t�H���g�l:C:\Users\(user)\Anaconda3\Scripts\activate.bat
REM Anaconda�C���X�g�[�����ύX���Ă��Ȃ���ΕύX�s�v
set batfile="%USERPROFILE%\Anaconda3\Scripts\activate.bat"

REM �ȍ~�\�[�X////////////////////////////////////////////////////////////////////////////
REM �J�����g�f�B���N�g����bat�t�@�C���̂���t�H���_�ɐݒ�
cd %~dp0

call %batfile%
call conda create -n %ProjectName% python=3.7 --yes

call conda activate %ProjectName%

REM �C���X�g�[���p��bat�t�@�C���������Ă���t�H���_(���ׂẴo�[�W����)
set batf=%~dp0install_bat\ALL

for /r %batf% %%f in (*.bat) do (
    echo filename = %%f
    call %%f
)

REM �C���X�g�[���p��bat�t�@�C���������Ă���t�H���_(Python3.7)
set batf=%~dp0install_bat\Python3.7

for /r %batf% %%f in (*.bat) do (
    echo filename = %%f
    call %%f
)

echo �C���X�g�[���̈�A�̏��������s���܂���

pause