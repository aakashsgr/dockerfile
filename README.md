# Autograding Example: Python
![GitHub manifest version](https://img.shields.io/github/manifest-json/v/aakashsgr/python?label=version&logo=GitHub)

This example project is written in python, and tested with pytest

# Tools Used:
* 'Visual Studio Code'

# Features
* Detailed info on failing assert statements (no need to remember self.assert* names)
* Auto-discovery of test modules and functions
* Modular fixtures for managing small or parametrized long-lived test resources
* Can run unittest (or trial), nose test suites out of the box
* Python 3.5+ and PyPy3
* Rich plugin architecture, with over 850+ external plugins and thriving community

# Install Dependencies 
```
python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```

```
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

# Testing Unit
> PyTest

PyTest helps to run all the tests in python

# Code Snippet

## Development Code
![development_code](./images/py_devcode1.PNG)
* create a class and define some objects

## Testing Code
![testing_code](./images/py_test1.PNG)
* well it was challenging one to call the class from the developmenet code
* use 'import sys' to import sys files
* give 'sys.path.append('../Python_App')' this helps system to look in the folder 'Python_App'
* from 'Python_App' folder import the class

## Output Screen
![Output_Screen](./images/py_output1.PNG)
* change the directory where testing file is present
* it got executed
* all the tests have passed!!!!
