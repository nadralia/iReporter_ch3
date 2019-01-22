[![Build Status](https://travis-ci.org/nadralia/iReporter_ch3.svg?branch=develop)](https://travis-ci.org/nadralia/iReporter_ch3)

# iReporter_ch3
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.


## Features
- Create (sign up) user account
- Sign in (login) to the app
- Create a incident record
- Get all incident records
- Get a specific incident record
- Edit a specific incident record.
- Delete an incident record
- Admin can change the status of a record to either under investigation, rejected (in the event of a false claim) or resolved (in the event that the claim has been investigated and resolved).


## API Endpoints
| Methods | EndPoint                               | Functionality                                   |Access
| ------- | -------------------------------------- | ----------------------------------------------- |------

### Technologies used to build the application
- `Python3` - A programming language that lets us work more quickly.
- `Flask` - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.
- `Virtualenv` - A tool to create an isolated virtual environment.
- `Git` - Version Control System for tracking your changes.

### Installation

Create a new directory and initialize git in it. Clone this repository by running

```sh
git clone https://github.com/nadralia/iReporter_ch3
```

Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using

```sh
virtualenv venv
```

Activate the virtual environment

```sh
cd venv/scripts/activate
```

Install the dependencies in the requirements.txt file using pip

```sh
pip install -r requirements.txt
```

Start the application by running

```sh
python run.py
```

## How to run tests

Enter the command below in the terminal to run the tests with coverage using
 pytest

```sh
  python -m pytest tests/
```

### Link to iReporter on Heroku


## Author

Adralia Nelson

## Acknowledgements

Big thanks to LFA's and fellow colleagues at [Andela](https://andela.com) for reviewing the project and the guiding on the basic principles.