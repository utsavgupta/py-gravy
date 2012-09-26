#!/usr/bin/env python

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../lib/"))

from pygravy import PyGravy
import unittest

class TestSuite(unittest.TestCase):
	def setUp(self):
		self.obj = PyGravy("   you@example.com		  ", True)

	def test_object_creation(self):
		self.assertEqual(self.obj.email, "you@example.com")
		self.assertEqual(self.obj.use_https, True)

	def test_properties(self):
		self.assertEqual(self.obj.avatar_rating, None)
		self.assertEqual(self.obj.avatar_default, None)
		self.assertEqual(self.obj.avatar_size, None)

		self.obj.avatar_rating = 'pg'
		self.obj.avatar_default = 'http://example.com/image.jpg'
		self.obj.avatar_size = 128

		self.assertEqual(self.obj.avatar_rating, 'pg')
		self.assertEqual(self.obj.avatar_default, 'http://example.com/image.jpg')
		self.assertEqual(self.obj.avatar_size, 128)

	def test_force_load_options(self):
		self.assertEqual(self.obj.params.has_key('f'), False)

		self.obj.avatar_set_force_load()
		self.assertEqual(self.obj.params['f'], 'y')

		self.obj.avatar_unset_force_load()
		self.assertEqual(self.obj.params.has_key('f'), False)

if __name__ == '__main__':
	unittest.main()