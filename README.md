# Document Presenter

## Requirements

Django 3.0

Python 3.8.0

Materialize 1.0

## Installation Steps

1. Install python 3.6 if not done already 
2. Download and extract application tar ball
3. Import the project to an IDE of your choice (I use PyCharm)
4. Setup project interpreter (setup python venv) and project structure.
5. Configure your database details in settings.py file.
6. Execute following commands to setup your database with necessary tables.
   ```
   <venv>/python manage.py makemigrations
   <venv>/python manage.py migrate
   ```
7. Create admin user for your application
   ```
   <venv>/python manage.py createsuperuser
   ```   
   create admin credentials when prompted 
8. Now run the application now application would be started in 8000 port.
   ```
   <venv>/python manage.py runserver
   ```
Live demo http://vibinmarish.pythonanywhere.com/

Homepage
   ![Alt text](https://github.com/vibinmarish/navigus_Round_2/blob/master/Screenshots/home.png "HomePage")
Signup
   ![Alt text](https://github.com/vibinmarish/navigus_Round_2/blob/master/Screenshots/signup.png "Signup")
After Signin
   ![Alt text](https://github.com/vibinmarish/navigus_Round_2/blob/master/Screenshots/signin.png "Signin")
View Document
  ![Alt text](https://github.com/vibinmarish/navigus_Round_2/blob/master/Screenshots/View.png "View")

