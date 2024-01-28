# Flask Application with Flask-Migrate

## Introduction

This is a Flask application that handles database migrations using Flask-Migrate, an extension that manages SQLAlchemy database migrations for Flask applications using Alembic.

## Installation

First, create a virtual environment and activate it:

```bash
python3 -m venv env
source env/bin/activate
```

Then, install the necessary packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Database Migration

With the virtual environment activated, you can apply the existing migrations with the following command:

```bash
flask db upgrade
```

Then each time the database models change, generate a new migration and upgrade:

```bash
flask db migrate
flask db upgrade
```

To sync the database in another system, just refresh the migrations folder from source control and run the upgrade command.

To see all the commands that are available, run this command:

```bash
flask db --help
```

## Running the Application

Finally, you can run the application:

```bash
flask run
```

## Resources

- Flask-Migrate Documentation
- Flask-Migrate GitHub
