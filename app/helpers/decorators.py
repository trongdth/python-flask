#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json

from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import request, g
from app import db
from app.helpers.response import response_error
from app.constants import USER_ROLE
from app.helpers.message import MESSAGE, CODE


def whitelist(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		blacklist_path = os.path.abspath(os.path.dirname(__file__)) + '/blacklist.json'
		try:
			with open(blacklist_path) as data_file:    
				data = json.load(data_file)
			ip = request.headers['X-Real-Ip']
			if ip is not None:
				ips = ip.split(',')
				if ips[0] in data:
					return response_error("Access deny!")
		except Exception as ex:
			print(str(ex))
		
		return f(*args, **kwargs)
	return wrap
