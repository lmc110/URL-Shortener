import flask
import os
import json
import base64
import uuid

app = flask.Flask(__name__)

urlDict = {}

if os.path.exists('bookmarks.json'):
    urlDict = json.load(open('bookmarks.json', 'r', encoding='UTF8'))


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    url = flask.request.form['url']
    key = base64.urlsafe_b64encode(uuid.uuid4().bytes)[:12]
    key = key.decode('utf-8')
    urlDict.update({key: url})
    with open('bookmarks.json', 'w') as f:
        json.dump(urlDict, f)
    return flask.redirect(flask.url_for('lookup', key=key) + '?preview=1', code=303)


@app.route('/<key>')
def lookup(key):
    pass

if __name__ == '__main__':
    app.run()