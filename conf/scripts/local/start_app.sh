#!/bin/bash
APP_NAME="" # update to app_name
MANAGER_NAME="pipenv" # update to manager_name options pipenv, python, poetry

APP_TARGET_FOLDER="applications"
BASE_DIR=`pwd`
FULL_DIR="${BASE_DIR}/${APP_TARGET_FOLDER}/${APP_NAME}"
echo "About creating ${APP_NAME} App in ${APP_TARGET_FOLDER} Folder"
echo "Current directory is ${BASE_DIR}"
echo "Full directory is ${FULL_DIR}"
if [ ${APP_NAME} ]
then
    if [ ${MANAGER_NAME} == "poetry" ]
    then
        mkdir ${FULL_DIR}
        python manage.py startapp ${APP_NAME} ./${APP_TARGET_FOLDER}/${APP_NAME}
    elif [ ${MANAGER_NAME} == "pipenv" ]
    then
        mkdir ${FULL_DIR}
        pipenv run python manage.py startapp ${APP_NAME} ./${APP_TARGET_FOLDER}/${APP_NAME}
    else
        mkdir ${FULL_DIR}
        python manage.py startapp ${APP_NAME} ./${APP_TARGET_FOLDER}/${APP_NAME}
    fi
fi