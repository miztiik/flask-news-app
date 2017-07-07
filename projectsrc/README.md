# flask-news-app

Python Flask app to fetch latest news from a variety of sources


The tree structure of the project looks like this.
```sh
.
├── projectsrc
│   ├── __init__.py
│   ├── README.md
│   ├── static
│   │   └── style.css
│   └── templates
│       ├── hotNews.html
│       └── Welcome.html
├── run.py
└── test_app.py

3 directories, 7 files
```

### News Fetcher
The `__init__.py` has the rss feed parser code and the various RSS links to new media sites hardcoded along with the `news relevancy timeline`

### Unit Tests
`test_app.py` has three test cases
 - Make a `GET` request for news page and check if http return code is `200`
 - Make a `POST` request and check if http return code is `200`
 - Make a `POST` request for invalid url and check return code is `302`
Please feel free to add to them