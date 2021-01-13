python --version 2>NUL
if errorlevel 1 goto errorNoPython
pyinstaller -v>NUL
if errorlevel 1 goto errorNoPyinstaller

pyinstaller --onefile --icon=pixel_book.ico main.py
copy config.json dist\config.json
pause
exit

:errorNoPython
echo.
echo Error^: Python not installed
pause
exit

:errorNoPyinstaller
echo.
echo Error^: Pyinstaller not installed
pause
exit
