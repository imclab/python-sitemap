
import unittest
from sitemap import *

class TestUrlSetElement(unittest.TestCase):
    
    def setUp(self):
        self.record = {
            'loc' : 'http://www.example.com',
            'lastmod' : '2005-01-01',
            'changefreq' : 'monthly',
            'priority' : '0.3'
        }

    def testCreateOnlyWithLocation(self):
        params = {
            'loc':'http://www.example.com'
        }
        e = UrlSetElement(**params)

    def testCreateFails_MissingLocation(self):
        params = {
            'changefreq' : 'daily',
            'priority' : '0.5'
        }
        try:
            e = UrlSetElement(**params)
            self.assertTrue(False)
        except ValueError:
            pass

    def testCreateFails_InvalidUrl(self):
        params = {
            'loc' : 'dummy-string'
        }
        try:
            e = UrlSetElement(**params)
            self.assertTrue(False)
        except InvalidUrl:
            pass

    def testCreateFails_InvalidLastMod(self):
        params = {
            'loc' : 'http://www.example.com/sitemap.xml',
            'lastmod' : '2005-13-35'
        }
        try:
            e = UrlSetElement(**params)
            self.assertTrue(False)
        except InvalidDate:
            pass

    def testCreateFails_InvalidChangeFreq(self):
        params = {
            'loc' : 'http://www.example.com/sitemap.xml',
            'changefreq' : 'dummy-value'
        } 
        try:
            e = UrlSetElement(**params)
            self.assertTrue(False)
        except InvalidChangeFreq:
            pass

    def testImmutableProperties(self):
        e = UrlSetElement(**self.record)
        try:
            e.loc = 'Something'
            self.assertTrue(False)
        except AttributeError:
            pass

