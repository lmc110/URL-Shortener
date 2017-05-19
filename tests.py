import os
import unittest

from main import app
from init import db
from models import Bookmark


class FlaskBookshelfTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app = app.test_client()
        db.create_all()
        self.app.testing = True

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_url(self):
        bookmark = Bookmark(url='www.google.com', key='1234abcd')
        db.session.add(bookmark)
        db.session.commit()
        self.assertEqual(bookmark.url, "www.google.com")

if __name__ == '__main__':
    unittest.main()



