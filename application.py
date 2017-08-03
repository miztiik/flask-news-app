#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script calls setsup gunicorn server to point to the applciation"""
from appsrc import application

if __name__ == "__main__":
    application.run()

# gunicorn --bind 0.0.0.0:8000 application &