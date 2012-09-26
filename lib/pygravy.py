"""
.. module:: pygravy
   :platform: Unix, Windows, Mac OS X
   :synopsis: A python library for generating Gravatar urls (gravylicious port).

.. moduleauthor:: Utsav Gupta
"""

# Copyright (c) 2012 Utsav Gupta

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
# associated documentation files (the "Software"), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the 
# following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions 
# of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.

import md5
import utils.common_filters

def Property(method):
	return property(**method())

class PyGravy(object):

	def __init__(self, email, use_https = False):
		"""
		This function is used for creating a new PyGravy object.

		:param email: The user's email address.
		:param use_https: A boolean argument used to specify whether or not to use the https protocol. By default it's set to false.
		
		Example:

		>>> from pygravy import PyGravy
		>>> gravatar = PyGravy('user@example.com')
		"""

		self.email = email.strip()
		self.use_https = use_https

		self.params = {}

		self.param_filters = { 'd': utils.common_filters.sanitize_url,
							   's': utils.common_filters.validate_size,
							   'r': utils.common_filters.validate_rating,
							 }

	def email_hash(self):
		"""
		This function returns the md5 hexadecimal digest of the email address.
		"""

		return md5.new(self.email).hexdigest()

	@Property
	def avatar_rating():
		doc = 	"""
				Rating property. Select from g, pg, r and x.

				Example:
				
				>>> gravatar.avatar_rating = 'r'
				>>> gravatar.avatar_rating
				'r'
				"""

		def fget(self):
			if self.params.has_key('r'): return self.params['r']
			return None
	    
		def fset(self, value):
			self.params['r'] = value

		def fdel(self):
			if self.params.has_key('r'): del(self.params['r'])
	    
		return locals()

	@Property
	def avatar_default():
		doc = 	"""
				Default avatar property. Lets you set the fallback avatar.
				You can use thr gravatar defaults identicon, monstericon, 404,
				mm, wavatar and retro.

				Example:
				
				>>> gravatar.avatar_default = 'somesite.com/image1.jpg'
				>>> gravatar.avatar_default
				'somesite.com/image1.jpg'
				"""

		def fget(self):
			if self.params.has_key('d'): return self.params['d']
			return None
	    
		def fset(self, value):
			self.params['d'] = value

		def fdel(self):
			if self.params.has_key('d'): del(self.params['d'])
	    
		return locals()

	@Property
	def avatar_size():
		doc = 	"""
				Size property. Assign the desired size of the avatar (in pixels).

				Example:

				>>> gravatar.avatar_size = 128
				>>> gravatar.avatar_size
				128
				"""

		def fget(self):
			if self.params.has_key('s'): return self.params['s']
			return None
	    
		def fset(self, value):
			self.params['s'] = value
	    
		def fdel(self):
			if self.params.has_key('s'): del(self.params['s'])

		return locals()

	def avatar_set_force_load(self):
		"""Loads the fallback avatar by default."""

		self.params['f'] = 'y'

	def avatar_unset_force_load(self):
		"""Reverses the action of avatar_force_load."""

		if self.params.has_key('f'): del(self.params['f'])

	def avatar_url(self):
		"""Returns a link to the desired gravatar."""

		protocol = "http"
		domain_name = "gravatar.com"
		avatar_path = "/avatar/" + self.email_hash()
		parameters = []

		if self.use_https:
			protocol += 's'
			domain_name = "secure." + domain_name

		if len(self.params) > 0:
			for param, value in self.params.items():

				if self.param_filters.has_key(param): value = self.param_filters.get(param)(value)

				key_value = '='.join(map(str, (param, value)))

				parameters.append(key_value)

		parameters = '&'.join(parameters)

		return '?'.join((protocol + "://" + domain_name + avatar_path, parameters))
