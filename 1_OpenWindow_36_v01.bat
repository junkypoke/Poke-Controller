@echo off
REM ���[�U�[�ϐ�//////////////////////////////////////////////////////////////////////////
REM �v���W�F�N�g��
REM �f�t�H���g�l	:PokeCon3_6
REM ���l:0_CreatEnv.bat�ɂ���v���W�F�N�g���Ɠ����ɂ��邱��
set ProjectName="PokeCon3_6"

REM activate.bat�̕ۑ��ꏊ
REM �f�t�H���g�l:C:\Users\(user)\Anaconda3\Scripts\activate
REM Anaconda�C���X�g�[�����ύX���Ă��Ȃ���ΕύX�s�v
set batfile="%USERPROFILE%\Anaconda3\Scripts\activate.bat"

REM �ȍ~�\�[�X////////////////////////////////////////////////////////////////////////////

call %batfile%
call conda activate %ProjectName%

set cd_tmp=%~dp0
set cd_tmp2=%cd_tmp%SerialController
cd %cd_tmp2%
echo �\�t�g���N�����܂�

REM Poke-Controller�N��
python Window.py
pause
