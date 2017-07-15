##################################################################################
## 
## VERSION      :   0.0.1
## DATE         :   15Jul2017
##
## DESCRIPTION  :   "Build RSS NEWS Feed Parser in Alpine linux"
##
## Ref [1]      :   http://mherman.org/blog/2015/03/06/node-with-docker-continuous-integration-and-delivery/
## Ref [2]      :   http://blog.hypriot.com/post/docker-compose-nodejs-haproxy/
## How-To Build :   docker build -t "flask-news-app" .
## How-To Run   :   docker run -dti --name t1 -p 8000:8000  flask-news-app bash
##################################################################################
FROM jfloff/alpine-python
MAINTAINER mystique

# Setup the Virtual Environment
RUN pip install virtualenv gunicorn

# Setup the App environment
RUN cd /var \
    && git clone https://github.com/miztiik/flask-news-app.git \
    && cd /var/flask-news-app \
    ### Create a Virtual Environment for our App
    && virtualenv /var/flask-news-app \
    && source /var/flask-news-app/bin/activate \
    ### Install the App dependencies
    && pip install -r requirements.txt

# make port 8000 available outside of the image
EXPOSE 8000

# apk update && apk add ca-certificates && update-ca-certificates && apk add openssl

# Start the `gunicorn` and bind it port `8000` and listen on all interfaces
# CMD [ "sh", "-c", "echo $HOME" ]
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "wsgi:APP", "&"]
