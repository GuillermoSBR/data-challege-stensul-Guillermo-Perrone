# Data Challenge
The following setup is a recomendatio but you are free to use any IDE of your choosing
## Content Index
- [Data Challenge](#data-challenge)
  - [Content Index](#content-index)
  - [Prepare Environment](#prepare-environment)
    - [IDEs Configuration](#ides-configuration)
    - [Run Tests](#run-tests)

## Prepare Environment
The following section will give you the steps to configure an environment you need to create new data challenge or run the tests locally.

1. Create a Python virtual environment `mkvirtualenv --python=/usr/local/opt/python@3.9/bin/python3.9 <virtual-env-name>`.
2. In order to contribute, install the required development packages `pip install -r requirements-dev.txt`.
3. Install the required runtime packages `pip install -r requirements.txt`.

### IDEs Configuration
IntelliJ / Pycharm should import this project without issues. You may want to configure a couple of things though:
- Set the project's Python interpreter pointing to `<virtual-env-name>` virtual env:
    - File -> Project Structure -> SDKs -> Add Python SDK -> Virtualenv environment -> <choose the existing one under `~/.virtualenvs/<virtual-env-name>/bin/python` dir>
- Set the project's testing framework:
    - Preferences -> Tools -> Python integrated tools -> Testing -> Default test runner -> Choose `pytest`

### Run Tests

```sh
$ pytest ./test
```
