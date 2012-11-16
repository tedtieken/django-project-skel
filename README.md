{% if False %}
# Django 1.4 Project template with Bootstrap for fast Heroku deployment


## About

This is '''work in progress''' starting template for Django 1.4 projects.


## Features ##

* NOT YET REVIEWED FOR ACCURACY IN TEDTIEKEN VERSION
* Global assets, web, templates and fixtures directory.
* Collects static and media into public/{static,media} respectively.
* Django admin activated by default.
* Django timezone setting changed to UTC for sanity.
* HTML 5 base template with simple 404 and 500 error templates.
* Discourages storing credentials and secrets in the repository.
* Encourages the use of developer/machine specific `settings.py` file.
* Encourages the use of virtualenv and virtualenvwrapper.
* Encourages the use of pip and `requirements.txt`.
* Encourages the use of git.
* Includes a .gitignore for the usual junk.
* Automatically builds a README with installation notes.

## How to use this template to create your project ##

* https://gist.github.com/3266518
* Run the following one of the following commands, specifying your project name:
            
    * To use Twitter's Bootstrap
    
            django-admin.py startproject --template https://github.com/tedtieken/django-project-skel/zipball/master --extension py,md,gitignore,dist yourprojectname


{% endif %}


# {{ project_name|title }} Django Project #
## Prerequisites ##

- python >= 2.7
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages {{ project_name }}-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages {{ project_name }}-env
cd {{ project_name }}-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> {{ project_name }}
```

### Install requirements ###
```bash
cd {{ project_name }}
pip install -r requirements.txt
```

### Configure project ###
```bash
cp {{ project_name }}/__local_settings.py {{ project_name }}/local_settings.py
vi {{ project_name }}/local_settings.py
```

### Sync database ###
```bash
python manage.py syncdb
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000
