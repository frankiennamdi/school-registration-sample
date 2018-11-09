## Requirement

Python 3.7 <br/>
pipenv

## Install Dependencies and Create Virtual Environment

1. At project root type to download all the dependency and create the virtual environment.
    `pipenv install`

2. To see where the virtual environment was created 

    `python --py`

This project was developed using vscode to continue developing with the IDE update the .vscode/settings.json **python.pythonPath** to the value from the command above.

## Running tests

1. Run pytest with no console outputs:

    `pipenv run python3 -m pytest`

2. Run pytest with console outputs:

    `pipenv run python3 -m pytest -s -v`

3. Run behave scenario tests with no debug outputs:

    `pipenv run python3 -m behave`

3. Run behave scenario tests with debug outputs:
    `pipenv run python3 -m behave -f plain --no-capture`

