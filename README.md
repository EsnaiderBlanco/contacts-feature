# Contacts APP 

Contacts APP was builded with Python3(Flask), the porpuse of the app is create a simple CRUD using SQLAlchemy library and PostgreSQL as database.

## Requirements

* A web browser such as [Google Chrome](https://www.google.com/chrome/) or [Firefox](https://www.mozilla.org/en-US/firefox/new/)

* [Python 3.6](https://www.python.org/downloads/) or newer.

* [pip](https://pip.pypa.io/en/stable/) - Python package manager.

* [PostgreSQL](https://www.postgresql.org/download/)

## Technologies

* Bootstrap 4
* Python 3.6
* SQLAlchemy 1.3
* PostgreSQL 10.10

## Installation

This app can be installed with git:

```bash
https://github.com/EsnaiderBlanco/contacts-feature.git
```

Use the package manager 'pip' to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage

```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

To run it locally.

```bash
flask run
```

After running the app, open up a web browser and go to

    localhost:5000

Or run it in your public IP.

```bash
flask run --host=0.0.0.0
```

Then go to:

    public-ip:5000

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
