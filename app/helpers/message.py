#!/usr/bin/python
# -*- coding: utf-8 -*-

class MESSAGE(object):
	# COMMON ERROR
	INVALID_PARAMETER = 'please double check your parameters.'
	INVALID_EMAIL = 'email is invalid'
	INVALID_PERMISSION = 'invalid permission'


	# USER
	USER_HAS_EMAIL_EXIST_ALREADY = 'email is existed'
	USER_NOT_FOUND = 'User not found!'
	PASSWORD_NOT_MATCH = 'Your password is incorrect, Please try again!'

	#Question
	EMPTY_QUESTION = 'Question list is empty!'


class CODE(object):
	# COMMON ERROR
	INVALID_PARAMETER = '1000'
	INVALID_EMAIL = '1001'
	INVALID_PERMISSION = '1002'

	# USER
	USER_HAS_EMAIL_EXIST_ALREADY = '2000'
	USER_NOT_FOUND = '2001'
	PASSWORD_NOT_MATCH = '2002'

	#Question

	EMPTY_QUESTION = '3000'

