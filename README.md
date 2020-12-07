# python-reference

https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Environment set up
1. change to project source directory
    - py -m venv env
    - run activate.bat
1.install packages
    - py -my pip install package
    
1. send all packages to a file for easy environment replication   
    - py -m pip freeze > requirements.txt
1. deactivate venv
    - run deactivate.bat

1. add venv to gitignore


1. read in file to install required packages
    - py -m pip install -r requirements.txt
