### Purpose

Here we have create the project user dashboard and app user management,
here we have defind the login page

### Steps to install and run store app on your local machine

* Run `$ sudo apt-get install python3.9-dev python3.9-venv` command to install virtual environment
* Run `$ source env/bin/activate` command to Create Virtual environment
* Run `$ pip install -r requirements.txt` command to Install project requirement file
* Set database name and password on your project Setting file
    * Go to setting.py file and update database connection in your setting file
      `DATABASES = {`
      `'default': {`
      ` 'ENGINE': 'django.db.backends.mysql',`
      `'NAME': ('DATABASE_NAME'),`
      `'USER': ('DATABASE_USER'),`
      `'PASSWORD': ('DATABASE_PASSWORD'),`
      `'HOST': ('DATABASE_HOST'),`
      `'PORT': ('DATABASE_PORT'),`
      `}`
      `}`
* Run `$ python manage.py migrate` command to apply migrations on your local machine
* Run `$ python manage.py runserver` command to run project on your local machine

