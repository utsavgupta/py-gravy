#!/usr/bin/env python

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../lib/"))

from pygravy import PyGravy
import unittest
import re

class TestSuite(unittest.TestCase):
	def setUp(self):
		self.obj = PyGravy("   you@example.com		  ", True)

	def test_size_filter(self):
		self.obj.avatar_size = 0
		self.assertRaises(Exception, self.obj.avatar_url)
		self.obj.avatar_size = 513
		self.assertRaises(Exception, self.obj.avatar_url)

	def test_size_rating(self):
		self.obj.avatar_rating = 'z'
		self.assertRaises(Exception, self.obj.avatar_url)
		self.obj.avatar_rating = 'pg'
		self.assertTrue(self.obj.avatar_url())

	def test_url_sanitization(self):
		self.obj.avatar_default = 'example.com/some_image<public[12]>.jpg'
		self.assertFalse(re.match('.*<.*\[.*\]>.*', self.obj.avatar_url()))

if __name__ == '__main__':
	unittest.main()