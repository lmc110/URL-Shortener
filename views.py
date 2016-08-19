import flask
import os
import json
import base64
import uuid
import models

from models import Bookmark
from init import db, app


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    #grab url from form
    url = flask.request.form['url']

    #generate key
    key = base64.urlsafe_b64encode(uuid.uuid4().bytes)[:12]
    key = key.decode('utf-8')

    #add url and key to database
    bookmark = models.Bookmark()
    bookmark.url = url
    bookmark.key = key
    db.session.add(bookmark)
    db.session.commit()
    return flask.redirect(flask.url_for('lookup', key=key) + '?preview=1', code=303)


@app.route('/<key>')
def lookup(key):
    #find key in database
    existing_bm = models.Bookmark.query.filter_by(key=key)

    #check if key in database
    if existing_bm is None:
        return flask.abort(404)

    #get url from object
    url = None
    for bm in existing_bm:
        url = bm.url

    #show preview page if 'preview' in browser url
    if 'preview' in flask.request.args:
        return flask.render_template('preview.html', key=key, url=url)
    else:
        return flask.redirect(url, code=301)


@app.errorhandler(404)
def page_not_found(err):
    return flask.render_template('404.html'), 404
