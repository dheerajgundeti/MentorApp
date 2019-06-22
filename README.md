# MentorApp

A django project for creating and maintaining the student database of various colleges

## Requirements

1. Django_2.1.1
2. Python 3 (3.6 used)
3. MYSQL

## Installation/setup process for testing the project

1. Create a database in your database server (eg. `onlinedb`)

2. open the file `server_configs/settings.py` and change the server credentials (ref. line no: 99-104)

3. Run command - ``python .\manage.py migrate`` from the root folder

4. Now finally it is ready for `runserver`
