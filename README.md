# default_django_setup
- starter template for other DjangoRest Framework projects.
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

This will install pre-commits lattest settings at .git/hooks/pre-commit.

# Directory Notes:
- New apps should go into the `Applications` Directory.
- Urls for each app should go into `Applications.urls.py` file.
- Django setting Constants should go into files that reside in the `conf.Addons` Directory.
- Database files should go into `conf.databases` Directory.
- Environmental variable files should go into `conf.env_variables` Directory.
- Scripts files should go into `conf.scripts` Directory.
- logs, templates, and media files can be found in `conf.miscellaneous` Directory.
- logic that can be used by applications should go into `conf.core` Directory.
- services like file management, emailing etc, should go into `services` Directory.
- All settings are registered in `conf.settings` Directory.

# Run into Problems?
Please create an issue if all doesnt go well, thanks.

# Was it helpful?
If this was helpful and resourceful to you, give me some `Star` rating.