# RSS News App written using Flask Framework

## Installation

### Runtime libraries
```sh
curl -O https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
&& yum -y install epel-release-latest-7.noarch.rpm
yum -y install python-pip git
pip install --upgrade pip
pip install virtualenv
cd /var
git clone https://github.com/miztiik/flask-news-app.git
cd /var/flask-news-app
```

### Create a Virtual Environment for our App
```sh
virtualenv /var/flask-news-app
source /var/flask-news-app/bin/activate
```

### Install the App dependencies
```py
pip install -r requirements.txt
```

## Start `gunicorn`
The built-in development server is single threaded, We will need a multithreaded server to support production workloads. We will be using `gunicorn` here,
```py
pip install gunicorn
```
Start the `gunicorn` and bind it port `8000` and listen on all interfaces

```py
gunicorn --bind 0.0.0.0:8000 application &
```

### Running as docker container
```sh
# Build using the attached docker file
docker build -t mystique/flask-news-app .

# (or easily) Pull the latest image from docker hub
docker pull mystique/flask-news-app

# Run the app
docker run -dti -p 8000:8000 --name newsapp docker pull mystique/flask-news-app

# If you want to override the port to any other custom port, say 80
docker run -dti -p 80:80 --name newsapp mystique/flask-news-app --bind 0.0.0.0:80
```

## Optional
Lets use `supervisor` to manage our gunicorn. It will run `gunicorn` server in the background and also start it automatically on reboot.

### Create `.conf` for Supervisord
```
touch /var/flask-news-app/flask-news-app-supervisor.conf
cat > << "EOF"
[program:flask-news-app-supervisor.conf]
command = /var/flask-news-app/bin/python
/home/deploy/.virtualenvs/flask-news-app/bin/gunicorn --bind 0.0.0.0:8000 wsgi:application -w 4
directory = /var/flask-news-app
# user = deploy
# stdout_logfile = /var/flask-news-app/logs/gunicorn/gunicorn_stdout.log
# stderr_logfile = /var/flask-news-app/logs/gunicorn/gunicorn_stderr.log
# redirect_stderr = True
environment = PRODUCTION=1
EOF
```

#### Update `supervisor` and Re-Start 
```sh
(flask-news-app) $ supervisorctl reread
(flask-news-app) $ supervisorctl update
(flask-news-app) $ supervisorctl start flask-news-app-supervisor
```


#### Setup NGNINX as WebServer

```sh
Client Request ----> Nginx (Reverse-Proxy)
                        |
                       /|\                           
                      | | `-> App. Server I.   127.0.0.1:8081
                      |  `--> App. Server II.  127.0.0.1:8082
                       `----> App. Server III. 127.0.0.1:8083
```

### About the Code
Python Flask application to fetch latest news from a variety of sources

### News Fetcher
The `__init__.py` has the RSS feed parser code and the various RSS links to new media sites hardcoded along with the `news relevancy timeline`

### Unit Tests
`test_app.py` has three test cases
 - Make a `GET` request for news page and check if http return code is `200`
 - Make a `POST` request and check if http return code is `200`
 - Make a `POST` request for invalid url and check return code is `302`

If you are interested, Please feel free to add to them :)

### To Do List
