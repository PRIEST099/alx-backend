#!/usr/bin/env python3
"""a simple flask app initialized wwitha simple htmls file"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    '''a simplel page that displays a title and a header'''

    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
