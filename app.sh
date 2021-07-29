#!/bin/sh

export FLASK_APP=flaskr
flask init-db && flask run -h 0.0.0.0 -p 8080

