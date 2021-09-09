@ECHO OFF
echo 本脚本将安装一个虚拟环境，作为程序运行环境
C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python -m pip install pipenv
C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python -m pipenv update
echo 安装完成，可以启动了
pause