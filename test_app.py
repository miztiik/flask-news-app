#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from projectsrc import app

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        app.config['TESTING'] = True
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        response = self.app.get('/newsSpider')
        # assert the status code of the response
        self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        response = self.app.post('/newsSpider', data=dict(newsSection="india"), follow_redirects=True)

        # assert the response data
        #self.assertEqual(response.data, "-#--#--#--#--#--#--#--#--#--#--#--#-")
        self.assertEqual(response.status_code, 200)

    def test_site_invalid_access(self):
        response = self.app.get('/admin_view_users')
        self.assertEqual(response.status_code, 302)


if __name__ == "__main__":
    unittest.main()
