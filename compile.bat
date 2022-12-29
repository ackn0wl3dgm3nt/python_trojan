@echo off

if "%1" == "payload" (
pyinstaller --hiddenimport win32timezone --onefile --name payload main.py
del payload.spec
)

if "%1" == "start" (
set script_name=start
set program_name=malware
set upx_dir=C:\UPX

pyinstaller --clean --onefile --noconsole --upx-dir %upx_dir% %script_name%.py --name %program_name%

del %program_name%.spec
)

if "%1" == "test" (
pyinstaller --onefile --noconsole test.py
copy dist\test.exe c:\users\user\desktop
del test.spec
)

rmdir /s /q build

