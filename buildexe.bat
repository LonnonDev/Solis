@ECHO OFF
type text.sol > dist/text.sol
echo toggle = True > onoff.py
pyinstaller --onefile main.py
echo toggle = False > onoff.py
"C:\Program Files\7-Zip\7z.exe" a -tzip -r "WindowsSolisX.X.X.zip" ".\dist\*"
pause