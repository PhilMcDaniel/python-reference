# python-reference

https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Environment set up
1. change to project source directory
    - py -m venv env
    - run activate.bat
1. install packages
    - manual: py -my pip install package
    - read from reqs: py -m pip install -r requirements.txt
1. send all packages to a file for easy environment replication   
    - py -m pip freeze > requirements.txt
1. deactivate venv
    - run deactivate.bat
1. add venv to gitignore
