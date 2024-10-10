@echo off
setlocal

:: Get the directory where the batch script is located
set "script_dir=%~dp0"

:: Output file location in the same directory as the script
set "output_file=%script_dir%SoftwareVersions.txt"

:: Clear the output file if it already exists
type nul > "%output_file%"

:: List installed software and their versions
echo Installed Software and Their Versions >> "%output_file%"
echo. >> "%output_file%"

:: List software using Get-WmiObject
powershell.exe -Command "Get-WmiObject -Class Win32_Product | Select-Object Name, Version | Format-Table -AutoSize" >> "%output_file%"

:: List python modules
echo. >> "%output_file%"
echo List python packages >> "%output_file%"
echo. >> "%output_file%"


:: List Python packages
pip freeze >> "%output_file%"


:: List Git version
echo. >> "%output_file%"
echo Git Version >> "%output_file%"
git --version >> "%output_file%"

:: List Docker version
echo. >> "%output_file%"
echo Docker Version >> "%output_file%"
docker --version >> "%output_file%"

:: List Visual Studio Code version
echo. >> "%output_file%"
echo Visual Studio Code version >> "%output_file%"
code --version >> "%output_file%"

:: End of script
endlocal
