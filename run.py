# run.py
"""This script calls the main __init__.py"""

from appsrc import APP

if __name__ == "__main__":
    APP.config['TEMPLATES_AUTO_RELOAD'] = True
    APP.run(debug=True, host="0.0.0.0")
