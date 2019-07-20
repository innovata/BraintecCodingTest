# Braintec Address Database


## Installation.


1. Download the package using git-CLI or Web-browser.

   1.1. Using Git
   - git clone https://github.com/innovata/braintec.git

   1.2. Using Web
   - Download ZIP file and unpacked it on your local computer. (https://github.com/innovata/braintec)

2. Move into the package-folder and Make a virtualenv of Python3.7

   - python3 -m virtualenv env

3. Install required packages.

   Move to python virtualenv.
   - project_name $ source env/bin/activate
   - pip install -r requirements.txt

4. Install PostgreSQL(v11).


## PostgreSQL Database Setup.


1. Run PostgreSQL server using App or Terminal.

   1.1. Using App
   - https://postgresapp.com (For MacOSX)
   - You can find other ways for your machine. (https://www.postgresql.org/download/)

   1.2. Using Terminal

   Connect to PostgreSQL Shell.
   - project_name $ psql
   - psql_username=# CREATE DATABASE exercise;
   Check out if exercise DATABASE is created.
   - psql_username=# \l


## Django Setup.

1. Setup Terminal Environment

   - export PSQL_USER=user_name
   - export PSQL_PW=user_password
   - export DEBUG_ON=True (Optional)

2. Setup PostgreSQL Table(Contact)

   - $ python manage.py makemigrations contact
   - $ python manage.py sqlmigrate contact 0001
   - $ python manage.py migrate
   Check out if "contact-contact" table is created.
   - psql_username=# \dt

3. Run Django Server

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
