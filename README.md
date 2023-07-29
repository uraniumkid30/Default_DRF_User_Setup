# default_django_setup
- starter template for other django (None API) projects.
- if you are looking for a quick way to start a new project 
with some things already available, like a customized user system and 
other services, then you are in the right place

# Requirements
pipenv
pyenv (python 3.9)
## Once pipenv is installed you can execute the following command
`pipenv sync`  This will install all the required package and
 also create a virtual environment if needed.

# HOWTO Development
 to use the development settings.  
Example:
```
pipenv run python manage.py command 
```

# How to run a script file
``` 
chmod u+x file.sh 
./file.sh
```

# HOW TO Contribute
Before First Commit or on update of the `.pre-commit-config.yaml` file, run :
either 
```
pre-commit install 
```
or 
```
pipenv run pre-commit install
```

This will install pre-commits lattest settings at .git/hooks/pre-commit

Also create an issue if all doesnt go well. thanks