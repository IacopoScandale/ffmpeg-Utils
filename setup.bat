@echo off

echo INSTALLING FFMPEG UTILS:
echo.

echo creating virtual environment ...
python -m venv venv
echo Done!
echo.

echo installing dependencies in virtual environment ...
call venv\Scripts\activate
pip install -e .
call venv\Scripts\deactivate

python post_install.py
echo Done!
echo.

echo Setup completed!
pause