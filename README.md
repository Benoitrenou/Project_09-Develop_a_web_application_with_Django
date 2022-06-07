This LitReview project is an Minimum Viable Product of an application for sharing reviews and opinions on books and articles.
The user can use the application to : 
  - request a review of a book/article from other users;
  - post their own review of a book/article;
  - follow users so that their posts (requests and reviews) appear on his personal feed.

This application was built using the Django framework in its version 3.2.9. The front-end was managed via Bootstrap.

The objectives of this project were:
    - Developp a web application using the framework Django
    - Use server-side rendering in Django
    - Build the frond-end pages using Bootstrap

Follow instructions below in order to launch the application.

## Create virtual environment

From your terminal, enter the following commands depending on your operating system

### With Linux/ MAC OS

    $ python -m venv <environment_name>
    example : python -m venv envlitreview
    
### With Windows:
    
    $ virtualenv <environment_name>
    example : virtualenv envlitreview 
    
## Activate virtual environment

### With Linux / MAC OS:

    $ source <environment_name>/bin/activate
    example : source envlitreview/bin/activate
   
### With Windows:

    $ source <environment_name>/Scripts/activate
    example : source envlitreview/Scripts/activate
    
## Installation of packages : 

    $ pip install -r requirements.txt

## Launch application

    $ python manage.py runserver

## Access to application

You can now access the application with your browser via [this address](http://127.0.0.1:8000/).

There is a demo profile that you can access by entering the following logins:

    Username: userdemo

    Password: projet09

This will give you access to a feed that already contains several publications.

You can also create your own profile via the registration page.
