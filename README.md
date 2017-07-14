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

# Start `gunicorn`
Start the `gunicorn` and bind it port `8000` and listen on all interfaces

```py
gunicorn --bind 0.0.0.0:8000 wsgi:APP &
```

## Optional
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
Python Flask app to fetch latest news from a variety of sources


### News Fetcher
The `__init__.py` has the RSS feed parser code and the various RSS links to new media sites hardcoded along with the `news relevancy timeline`

### Unit Tests
`test_app.py` has three test cases
 - Make a `GET` request for news page and check if http return code is `200`
 - Make a `POST` request and check if http return code is `200`
 - Make a `POST` request for invalid url and check return code is `302`

Please feel free to add to them