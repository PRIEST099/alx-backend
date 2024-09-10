#!/usr/bin/env python3
"""a simple flask app initialized wwitha simple htmls file"""


from flask import Flask, render_template


class Config():
    ''' A configuration class file'''

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)


app.config.from_object(Config)
babel = Babel(app, )


@app.route('/')
def home():
    '''a simplel page that displays a title and a header'''

    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
