# Author::    Utsav Gupta
# Copyright:: Copyright (c) 2012 Utsav Gupta
# License::   MIT License

from urllib import quote
import re

def sanitize_url(url):
	"""Returns a sanitized url."""
	return quote(url)

def validate_size(size):
	"""Raises an exception if the size is lesser than 1 or greater than 512."""
	
	if size < 1 or size > 512:
		raise Exception('Given size is out of range')

	return size

def validate_rating(rating):
	"""Raises an exception if the given rating is anything other than g, pg, r or x."""
	
	rating_regexp = re.compile('^(p?)g$|^r$|^x$')

	if rating_regexp.search(rating) is None: 
		raise Exception('Given rating is incorrect')

	return rating