@echo off
pyinstaller --onefile --noconsole --add-data assets;assets --hidden-import glcontext main.py
rmdir build /S /Q
rmdir __pycache__ /S /Q
pause
