#!/bin/sh
# OpenShift S2I adapter script

export FLASK_APP=flaskr

sleep ${INITIAL_DELAY:-0} &&
  flask init-db && flask run -h 0.0.0.0 -p ${PORT:-8080}

