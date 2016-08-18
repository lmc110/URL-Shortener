import flask
import os
import json

app = flask.Flask(__name__)

urlDict = {}

if os.path.exists('bookmarks.json'):
    urlDict = json.load(open('bookmarks.json', 'r', encoding='UTF8'))


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    pass


if __name__ == '__main__':
    app.run()