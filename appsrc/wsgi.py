#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script calls setsup gunicorn server to point to the applciation"""
from appsrc import APP

if __name__ == "__main__":
    APP.run()

# gunicorn --bind 0.0.0.0:8000 wsgi:APP &