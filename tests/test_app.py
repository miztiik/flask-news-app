#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The file has the unit tests that are to be run against our RSS Feed Parser
"""

import unittest
# from appsrc import application
import application

class FlaskAppTests(unittest.TestCase):
    """
    Class to contain the unit test cases
    """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        application.config['TESTING'] = True
        # creates a test client
        self.application = application.test_client()
        # propagate the exceptions to the test client
        self.application.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        """
        Make GET request to load the home page and get return code as 200
        """
        # sends HTTP GET request to the application
        # on the specified path
        response = self.application.get('/newsSpider')
        # assert the status code of the response
        self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        """
        Make POST request to load the results page and get return code as 200
        """
        # sends HTTP GET request to the application
        # on the specified path
        response = self.application.post('/newsSpider',\
                                 data=dict(newsSection="india"),\
                                 follow_redirects=True)

        # assert the response data
        #self.assertEqual(response.data, "-#--#--#--#--#--#--#--#--#--#--#--#-")
        self.assertEqual(response.status_code, 200)

    def test_site_invalid_access(self):
        """
        Make GET request for non-existent page to re-load and get return code as 200
        """
        response = self.application.get('/admin_view_users')
        self.assertEqual(response.status_code, 302)


if __name__ == "__main__":
    unittest.main()
