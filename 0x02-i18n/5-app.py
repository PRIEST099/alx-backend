#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    locale: str | None = request.args.get('locale')
    if (locale is not None) and (locale in app.config['LANGUAGES']):
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> dict | None:
    """Retrieves user information if the user exists in the dictionary."""

    user: str | None = request.args.get('login_as')
    if user is None:
        return None
    try:
        user_id: int = int(user)
    except ValueError:
        return None

    if user_id in users.keys():
        return {user_id: users[user_id]}
    return None


@app.before_request
def before_request() -> None:
    """ storing logged in user id on every request """
    g.user = get_user()


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
