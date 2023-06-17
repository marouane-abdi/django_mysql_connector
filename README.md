# django_mysql_connector

To set up a Django project using MySQL for submitting personal information, you'll need to perform the following steps:

Make sure you have Django and MySQL installed. You can install Django using pip, and MySQL can be installed separately or as part of a package such as XAMPP or WAMP.

Import the required modules in your Django project. In your Python file (e.g., views.py), add the following import statements:

pip install django 
pip install mysql.connector
from django.db import connection

Open the settings.py file located in the project's root directory

Locate the database settings section within settings.py and modify the following parameters to match your MySQL database configuration:

create the database name as 'mysqlconnect'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your_database_name>',
        'USER': '<your_mysql_username>',
        'PASSWORD': '<your_mysql_password>',
        'HOST': '<your_mysql_host>',
        'PORT': '<your_mysql_port>',
    }
}

Replace <your_database_name>, <your_mysql_username>, <your_mysql_password>, <your_mysql_host>, and <your_mysql_port> with the appropriate values specific to your MySQL setup.

Save the settings.py file after making the modifications.

Open a terminal or command prompt and navigate to your project's root directory using the cd command. For example:


cd app

Apply any pending database migrations by running the following command:

python manage.py makemigrations
python manage.py migrate

This command will create the necessary tables in your MySQL database based on your Django models.

Once the migrations are applied successfully, start the Django development server using the following command:

python manage.py runserver
The development server will start running, and you can access your Django application by opening a web browser and navigating to http://localhost:8000.

That's it! You have now set up your Django project with a MySQL database and started the development server.
