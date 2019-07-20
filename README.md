# Braintec Address Database


## Installation.


1. Download the package.

   - git https://github.com/innovata/braintec.git

   Or,

   - Download ZIP file and unpacked it on your local computer. (https://github.com/innovata/braintec)

2. Move into the package-folder and Make a virtualenv of Python3.7

   - python3 -m virtualenv env

3. Install required packages.

   - pip install -r requirements.txt

4. Install PostgreSQL(v11).


## PostgreSQL Database Setup.


1. Run PostgreSQL server using App or Terminal.

   1.1. Using App

   1.2. Using Terminal

   - (env) project_name $ psql
   - psql_username=# CREATE DATABASE exercise;
   - psql_username=# \l


## Django Setup.

1. Creating the Admin.

   1.1. Make admin migration.
   - $ python manage.py migrate

   1.2. register admin account info following the instruction.
   - $ python manage.py createsuperuser
   - Username: admin_name
   - Email address: admin_email
   - Password: admin_password

   1.3. Check out if admin can login.

   1.3.1. Run the server.
   - $ python manage.py runserver

   1.3.2. Open a browser and access to "localhost:8000/admin/"

   1.3.3. Login using admin_name, admin_password


2. Setup Terminal Environment

   - export PSQL_USER=user_name
   - export PSQL_PW=user_password
   - export DEBUG_ON=True (Optional)

3. Setup PostgreSQL Table(Contact)

   - $ python manage.py makemigrations contact
   - $ python manage.py sqlmigrate contact 0001
   - $ python manage.py migrate

4. Run Django Server

   - $ python manage.py runserver


## Run & Test.


1. Access to Main page.
   - http://localhost:8000/

2. Add a new contact info by input-box.
   - Type in some blanks and push the "Send" button.
   If there is an error, retry it based on the error message.

3. Add a new contact info by XML
   - Choose a test.xml file (Location : ./contact/data/test.xml) and push the "Send" button.
   - Just push the button without uploading the xml file. And retry it based on the error message.
