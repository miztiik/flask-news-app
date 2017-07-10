# run.py
"""This script calls the main __init__.py"""

from appsrc import app

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host="0.0.0.0")
