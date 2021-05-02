@ECHO OFF
echo toggle = True > onoff.py
pyinstaller --onefile main.py
echo toggle = False > onoff.py
pause