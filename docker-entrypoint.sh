#!/bin/bash

# Start Gunicorn processes
echo "Starting Gunicorn"
exec gunicorn appsrc.wsgi:application \
    --name flask-news-app \
    --bind 0.0.0.0:8000 \
    --pythonpath '/var/flask-news-app'
    "$@"