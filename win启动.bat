@echo off
start startserver.bat
for /f "tokens=3,4" %%a in ('"reg query HKEY_CLASSES_ROOT\http\shell\open\command"') do (set SoftWareRoot=%%a %%b)
start % SoftWareRoot % http://localhost:5000
exit