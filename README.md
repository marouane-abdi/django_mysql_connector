# django_mysql_connector
Django project using mysql  for submitting Personnal information 

Before running your Django project, there are a few configuration changes you need to make to connect it to your MySQL database.

1 - Open the settings.py file located in the project's root directory.

2 - Locate the database settings section and modify the following parameters to match your MySQL database configuration:


'ENGINE': 'django.db.backends.mysql',
'NAME': '<your_database_name>',
'USER': '<your_mysql_username>',
'PASSWORD': '<your_mysql_password>',
'HOST': '<your_mysql_host>',
'PORT': '<your_mysql_port>',
3 - Save the settings.py file.

4 - Running the Django Project

  To run your Django project, follow these steps:

  Open a terminal or command prompt.

5 - Navigate to your project's root directory using the cd command. For example:


cd app
6 Apply any pending database migrations by running the following command:


  python manage.py migrate
  Once the migrations are applied successfully, start the Django development server using the following command:


  python manage.py runserver
The development server will start running, and you can access your Django application by opening a web browser and navigating to http://localhost:8000.

That's it! You have now set up your Django project with a MySQL database and started the development server. You can customize your project further and build your desired interfaces using Bootstrap.
