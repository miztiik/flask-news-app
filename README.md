# RSS News App written using Flask Framework

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

### Fetch the code
```sh
git clone https://github.com/miztiik/flask-news-app.git
```