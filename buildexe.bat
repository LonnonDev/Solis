@ECHO OFF
type text.sol > dist/text.sol
(echo toggle = True && echo debugmode = False) > ./onoff.py
pyinstaller --onefile main.py --icon=soleado.ico
(echo toggle = False && echo debugmode = True) > ./onoff.py
"C:\Program Files\7-Zip\7z.exe" a -tzip -r "WindowsSolisX.X.X.zip" ".\dist\*"
pause