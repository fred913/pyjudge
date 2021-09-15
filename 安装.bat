@ECHO OFF
echo Preparing for a new virtualenv with packages needed...
python -m pip install pipenv
python -m pipenv update
echo Updated successfully!
pause
