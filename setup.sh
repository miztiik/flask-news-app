#!/bin/bash
set -ex

### Install Runtime libraries
curl -O https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
&& yum -y install epel-release-latest-7.noarch.rpm
yum -y install python-pip git
pip install --upgrade pip
pip install virtualenv

# Clone our app from git
cd /var
git clone https://github.com/miztiik/flask-news-app.git
cd /var/flask-news-app

### Create a Virtual Environment for our App
virtualenv /var/flask-news-app
source /var/flask-news-app/bin/activate

### Install the App dependencies
pip install -r requirements.txt
pip install gunicorn

# Start `gunicorn`
# Start the `gunicorn` and bind it port `8000` and listen on all interfaces
gunicorn --bind 0.0.0.0:8000 appsrc:application &

# Deactivate
deactivate

