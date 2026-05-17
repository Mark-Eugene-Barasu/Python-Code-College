# Python Code College 


1. Create a virtual environment: (374)
   python -m venv ll_env

2. Activate the virtual environment: (375)
   ll_env\Scripts\activate    
  

3. Install Django: (375)
   pip install Django

4. Create your Django project (the book calls it "learning_log") contains settings and main configuration: (376)
   django-admin startproject learning_log .

5. Create the database:(376)
   python manage.py migrate

6. Run the development server: (377)
   python manage.py runserver

7. Then open your browser and go to http://localhost:8000 (Check output on page 378)

8. Create your first app (learning_logs)  contains the actual features/functionality:(379)
   python manage.py startapp learning_logs 

-----------------------------------------------------------------------------------------------
1. Register the app in settings.py (380)

   Open learning_log/settings.py
   Find the INSTALLED_APPS list (around line 33)
   Add 'learning_logs', to the list. 

2. Define your first model: (379)

   Open learning_logs/models.py
   The book will guide you to create a Topic model
------------------------------------------------------------------------------------------------
Next, we need to tell Django to modify the database so it can store information related to the model Topic. (381)

  python manage.py makemigrations learning_logs
  python manage.py migrate
-------------------------------------------------------------------------------------------------
1.  Create a superuser account: (382)
    python manage.py createsuperuser

    Username (choose anything you like)    
    Email address (you can leave it blank by pressing Enter)
    Password (type it twice - it won't show on screen) 

2.  Register the Topic model with the admin site: (382 - 383)
    Open learning_logs/admin.py
    Replace the content with this code:

           from django.contrib import admin
           from .models import Topic
           admin.site.register(Topic)

3.  Start the server and test it:
    python manage.py runserver
    Then go to: http://127.0.0.1:8000/admin

--------------------------------------------------------------------------------------------------
Now test adding a Topic (383 test the Django administration)

   Click on "Topics" (or the "Add" link next to Topics)
   Add a topic like "Chess" or "Rock Climbing" 
   Click Save
-------------------------------------------------------------------------------------------------
What's Next (following Chapter 18)
1.  Create the Entry model - for journal entries related to each topic  (p 384) 
      After saving, run:
      python manage.py makemigrations learning_logs
      python manage.py migrate
2.  Register Entry in admin.py - so you can add entries through the admin (p 385)
    Start the server: python manage.py runserver
    Go to the admin page: http://127.0.0.1:8000/admin
3.  Add some entries - write some learning log entries for your topics from page 385 - 286

------------------------------------------------------------------------------------------------
Now you'll start building the actual web pages (the front-end) that users will see.

1. Creating a home page - mapping URLs and creating views

Step 1: Create a view in learning_logs/views.py  (390)
        Add a function for the home page (the book will show you the code)

Step 2: Create learning_logs/urls.py   (p 389)
        Create this NEW file and add URL patterns for your app

Step 3: Update the main learning_log/urls.py  (p 389)
        Connect your app's URLs to the main project

Step 4: Create the templates folder and HTML file
        Create folder: learning_logs/templates/learning_logs/
        Create file: index.html inside that folder  (p 391)

Step 5: python manage.py runserver and check http://127.0.0.1:8000/
    

2. Create the base template:
 
Step 1: Inside learning_logs/templates/learning_logs/, create a file called base.html (p 392 -393)

Step 2: Now Update index.html to use the base template (p 393)

Step 3: Now update learning_logs/urls.py (p 394)

Step 4: Now update learning_logs/views.py (p 395)

Step 5: learning_logs/templates/learning_logs/ topics.html (p 395 -396)

Step 6: Update learning_logs/templates/learning_logs/ base.html (p 396)

Step 7: Update learning_logs/urls.py (p 397)

Step 8: Update learning_logs/views.py (p 398)

Step 9: Update learning_logs/templates/learning_logs/ topic.html (p 398 -399)

Step 10: Update learning_logs/templates/learning_logs/ topics.html (p 399)

Step 11: Run:  python manage.py runserver  and check: http://127.0.0.1:8000/topics/1/

--------------------------------------------------------------------------------------------------
Chapter 19
----------
----------

Step 1: Create a new file in your learning_logs/forms.py (p 404)

Step 2: Update learning_logs/urls.py (p 405)

Step 3: Update learning_logs/views.py (p 405)

Step 4: Create a new file learning_logs/templates/learning_logs/ new_topic.html (p 407)

Step 5: Update learning_logs/templates/learning_logs/ topics.html (p 407)

Step 6: Update learning_logs/forms.py (p 408)

Step 7: Update learning_logs/urls.py (p 409)

Step 8: Update learning_logs/views.py (p 409)

Step 9: Create a new file learning_logs/templates/learning_logs/ new_entry.html (p 410)

Step 10: Update learning_logs/templates/learning_logs/ topic.html (p 411)

Step 11: Update learning_logs/urls.py (p 412)

Step 12: Update learning_logs/views.py (p 412)

Step 13: Create a new file learning_logs/templates/learning_logs/ edit_entry.html (p 413)

Step 14: Update learning_logs/templates/learning_logs/ topic.html (p 414)

Step 15: Create a new app called accounts (p 415)

Step 16: Update the learning_log/settings.py (p 415)

Step 17: Update the learning_log/urls.py (p 416)

Step 18: Create a new file accounts/urls.py (p 416)

Step 19: Create a new file & folders accounts/templates/registration/login.html (p 417)

Step 20: Update the learning_log/settings.py (p 418)

Step 21: Update learning_logs/templates/learning_logs/ base.html (p 418)

Step 22: Update learning_logs/templates/learning_logs/ base.html (p 419)

Step 23: Update the learning_log/settings.py (p 420)

Step 24: Update the accounts/urls.py (p 420)

Step 25: Update the accounts/views.py (p 421)

Step 26: Create a new file & folders accounts/templates/registration/register.html (p 422)

Step 27: Update learning_logs/templates/learning_logs/ base.html (p 422)

Step 28: Update the learning_logs/views.py (p 423)

Step 29: Update the learning_log/settings.py (p 424)

Step 30: Update the learning_logs/views.py (p 424 - 425)

Step 31: Update the learning_logs/models.py (p 425)

Step 32: Migrating the Database (p 426) Run the following:
                                          python manage.py makemigrations learning_logs
                                          When it asks you to select a fix, type 1 and press Enter.
                                          When it asks for a default value, enter 1 
                                          python manage.py migrate

Step 33: Update the learning_log/views.py (p 428)

Step 34: Update the learning_logs/views.py (p 428)

Step 35: Update the learning_logs/views.py (p 429)

Step 36: Update the learning_logs/views.py (p 430)

------------------------------------------------------------------------------------------------
Chapter 20
-----------
-----------

Step 1: Install bootstrap - pip install django-bootstrap5 (p 434)

Step 2: Update the learning_log/settings.py (p 434)

Step 3: Update learning_logs/templates/learning_logs/ base.html (p 435 - 440) 

Step 4: Update learning_logs/templates/learning_logs/ index.html (p 440 - 441)

Step 5: Update accounts/templates/registration/login.html (p 441 - 442)

Step 6: Update learning_logs/templates/learning_logs/ topics.html (p 442 - 443)

Step 7: Update learning_logs/templates/learning_logs/ topic.html (p 443 - 444)

Step 8: Installing platformshconfig -  pip install platformshconfig (p 446)

Step 9: Creating a requirements.txt File -  pip freeze > requirements.txt (p 446)

Step 10: Create a new file Tutorial 3/ requirements_remote.txt (p 447)

Step 11: create a new file Tutorial 3/ .platform.app.yaml (p 448 - 449)

Step 12: create a new folder and file Tutorial 3/ .platform/ routes.yaml (p 450)

Step 13: Update the learning_log/settings.py (p 451)

Step 14: python manage.py runserver  and check http://127.0.0.1:8000/

-----------------------------------------------------------------------------------------
---------------------------------

Only if you have an error saying:
You have a database migration issue. The error no such column: learning_logs_topic.owner_id means your database doesn't have the owner_id column that your code is expecting.


do the following:
Step 1: python manage.py makemigrations learning_logs
        Select an option: 1
        enter >>> 1 here as well

Step 2: python manage.py migrate

Step 3: python manage.py runserver then check http://127.0.0.1:8000/

----------------------------------------------------------------------------------------------------

IF you want to see all the users

Step 1: Go to: http://127.0.0.1:8000/admin/

Step 2: Log in with your superuser credentials (Username Passsowrd)

Step 3: Click on "Users" under the "Authentication and Authorization" section

------------------------------------------------------------------------------------------
view all the topics 

step 1: http://127.0.0.1:8000/admin/learning_logs/topic/