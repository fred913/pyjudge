@ECHO OFF
echo Preparing for a new virtualenv with packages needed...
python3 -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
python3 -m pip install pipenv
python3 -m pipenv update
python -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install pipenv
python -m pipenv update
python -m pip install requests
python3 -m pip install requests

echo Updated successfully!
pause
