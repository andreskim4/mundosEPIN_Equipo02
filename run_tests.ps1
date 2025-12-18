$ErrorActionPreference = "Stop"
$workspacePath = "C:\Users\AndrésKim\Desktop\DevOps proyecto 1\mundosEPIN_Equipo02-main\mundosEPIN_Equipo02-main"
Set-Location "$workspacePath\app"
python manage.py test --verbosity=2

