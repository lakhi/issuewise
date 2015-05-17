## INSTALLATION INSTRUCTIONS


1. install virtualenv using

    pip install virtualenv
    
2. create a folder called envs below the repository root 

    mkdir envs && cd envs
    
3. create a virtualenv

    virtualenv my_env
    
4. run the following command to activate the virtualenv

    source my_env/bin/activate  
    
5. install requirements by running the following command in the activated vitualenv
( the requirement file is located at requirements/dev_DC_requirements.txt)

    pip install -r *path to requirements file*
    
6. create a shell script env_vars.sh and put it somewhere safe (NOT in the
repository because this contains sensitive info and should not be commited
to the cloud)

    export MY_EMAIL_PASSWORD='blablabla'
    export MY_EMAIL_ID='something@somewhere.com'
    
 if you are using highly secure emailing services like gmail, you may need to 
 activate 2 step authentication and request a one time password for this 
 django app to use. For gmail, instructions can be found
 <a href=https://support.google.com/accounts/answer/185833?hl=en>here</a>
 
7. export the environment variables in your terminal session by running

    source *path to env_vars.sh*

8. now go inside the django project root issuewise directly below the repository
root. run the following commands to set up a sqlite database (for testing).

    python manage.py makemigrations
    python manage.py migrate
    
9. once the database has been set up successfully, start the development 
server using

    python manage.py runserver
    
if everything was fine till now, the API (comes with a cool frontend :D)
will become available at 127.0.0.1:8000

When you finish working on issuewise, you might want to run this command 
to get out of the virtualenv and back to where you were before

    deactivate
    
Also note that at the moment, we only have frontend available for 
HTTP BasicAuthentication. If you want to use Token Authentication 
instead, please uncomment the following lines in the settings file 
(which can be found at repository_root/issuewise/issuewise/base.py)

    REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
    }
    
The API documentation is also coming up soon. But before it does, 
shoot any questions to dibyachakravorty@gmail.com.

Happy testing :) Cheers!       
    
    

