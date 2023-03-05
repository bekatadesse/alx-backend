#!/usr/bin/env python3
"""
This module contains a Flask app that uses the Babel library to select the best
supported language based on the user's browser preferences.
"""

from typing import List

from babel import negotiate_locale
from flask import Flask, request, g, render_template
from flask_babel import Babel


class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Select the best supported language based on the user's browser preferences.

    Returns:
        A two-letter language code (e.g., 'en', 'fr', 'es').
    """
    user_languages = [lang for lang, _ in request.accept_languages]

    # Select the best supported language based on user's preferences
    locale = negotiate_locale(user_languages, app.config['LANGUAGES'])

    # If no supported language is found, return the default language
    return locale or app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index() -> str:
    """Render the index page."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
