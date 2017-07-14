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
###### python /var/flask-news-app/run.py
```py
gunicorn --bind 0.0.0.0:8000 wsgi:APP &
```

# Optional
Lets use `supervisor` to manage our gunicorn

### About the Code
Python Flask app to fetch latest news from a variety of sources

The tree structure of the project looks like this.
```sh
.
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── activate_this.py
│   ├── chardetect
│   ├── easy_install
│   ├── easy_install-2.7
│   ├── flask
│   ├── pip
│   ├── pip2
│   ├── pip2.7
│   ├── python -> python2
│   ├── python2
│   ├── python2.7 -> python2
│   ├── python-config
│   └── wheel
├── flask-news-app
│   ├── appsrc
│   ├── README.md
│   ├── requirements.txt
│   ├── run.py
│   └── test_app.py
├── include
│   └── python2.7 -> /usr/include/python2.7
├── lib
│   └── python2.7
├── lib64 -> lib
└── pip-selfcheck.json

```

### News Fetcher
The `__init__.py` has the rss feed parser code and the various RSS links to new media sites hardcoded along with the `news relevancy timeline`

### Unit Tests
`test_app.py` has three test cases
 - Make a `GET` request for news page and check if http return code is `200`
 - Make a `POST` request and check if http return code is `200`
 - Make a `POST` request for invalid url and check return code is `302`
Please feel free to add to them