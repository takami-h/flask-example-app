#!/bin/sh
# OpenShift S2I adapter script

export FLASK_APP=flaskr
flask init-db && flask run -h 0.0.0.0 -p ${PORT:-8080}

