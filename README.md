## Welcome to
# Master Exam System (MAS)


### About the Project

soon...

### About the BackEnd

soon...

### About the FrontEnd
You can view project in github with link: 


***

## Tech

* [Django](https://www.djangoproject.com/) - is a high-level `Python Web framework`
* [Django REST framework](https://www.django-rest-framework.org/) - `Django REST Framework` is a powerful and flexible toolkit for building Web `APIs`
* [PostgreSQL](https://www.postgresql.org/) - open source object-relational database system

And many other libraries.

Dillinger requires [Python](https://www.python.org) `v3.10` or `v3.11`.

```shell
$ git clone git@github.com:Abduraxmonnn/MasterExamSystem.git
$ cd master_exam_system
```

***

## Setting project

* `Linux`
```shell
$ virtualenv -p /usr/bin/python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

* `Windows`
```shell
$ python -m venv ./venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

* `MacBook`
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

***

## Development
### Configure `PostgreSQL`
Create clear database named `master_sys_db`.

Create `master_sys_user` db user with password `master_12345` and grand privileges to him.

If you want to create a database with a different name, user and password, you can change the initial configuration to your own configuration.
```shell
$ sudo -u postgres psql
postgres=# ...
CREATE DATABASE master_sys_db;
CREATE USER master_sys_user WITH PASSWORD 'master_12345';
ALTER ROLE master_sys_user SET client_encoding TO 'utf8';
ALTER ROLE master_sys_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE master_sys_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE master_sys_db TO master_sys_user;
\q
```
Migrate to database and run project.
```shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
`Output`
```shell
System check identified no issues (0 silenced).
Month date, year - hh:mm:ss
Django version 4.1.7, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Open http://127.0.0.1:8000 in your browser for see result.
