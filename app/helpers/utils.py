#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import json
import time
import calendar
import hashlib

from fractions import Fraction
from datetime import datetime
from time import gmtime, strftime
from flask import g


def is_valid_email(email):
	if email is not None:
		email = email.lower()
		if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,6})$", email) != None:
			p = email.split('@')
			if p[1] is not None and p[1] not in ['spam4.me', 'pokemail.net', 'guerrillamailblock.com', 'guerrillamail.org', 'guerrillamail.net', 'guerrillamail.de', 'guerrillamail.com', 'guerrillamail.biz', 'grr.la', 'guerrillamail.info', 'sharklasers.com', 'yopmail.com', 'nopemail.me', 'maildrop.cc', 'proove.org', 'izolrom.ro', 'voltaer.com', 'shayzam.net', 'yevme.com', 'opayq.com', 'emailna.co', 'tuta.io', 'getnada.com', 'moruzza.com', 'mailhex.com', 'radiodale.com', 'datasoma.com', 'providier.com', 'cliptik.net', 'plutofox.com', 'lagify.com', 'khtyler.com', 'shayzam.ne', 'geroev.net', 'nando1.com', 'zdfpost.net', 'tempmail.ws']:
				return True
	return False


def is_valid_password(password):
	if len(password) >= 3:
		return True
	return False


def is_valid_name(name):
	if len(name.strip()) == 0:
		return False
	return True


def parse_date_to_int(input):
	delta = input - datetime.now()
	return delta.seconds


def isnumber(s):
   try:
	   float(s)
	   return True
   except ValueError:
	   try:
		   Fraction(s)
		   return True
	   except ValueError:
		   return False


def parse_date_string_to_timestamp(date_str):
	dt_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').strftime('%s')
	return int(dt_obj)


def local_to_utc(t):
	secs = time.mktime(t)
	return calendar.timegm(time.gmtime(secs))


def utc_to_local(t):
	secs = calendar.timegm(t)
	return time.localtime(secs)


def current_milli():
	return int(round(time.time() * 1000))


def second_to_strftime(seconds, format='%b %d %Y %I:%M:%S %p', is_gmt=False):
	# '%Y-%m-%d %H:%M:%S'
	text = datetime.fromtimestamp(seconds).strftime(format)
	if is_gmt:
		text = '{} {}'.format(text, strftime("%z", gmtime()))
	return text


def now_to_strftime(format='%b %d %Y %I:%M:%S %p'):
	return datetime.now().strftime(format)