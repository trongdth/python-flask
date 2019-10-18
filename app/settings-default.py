import os
from datetime import timedelta


class BaseConfig(object):
	ENV = 'DEV'
	BASE_URL = ''
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))
	UPLOAD_DIR = os.path.join(BASE_DIR, 'files', 'temp')
	DOWNLOAD_DIR = os.path.join(BASE_DIR, 'files', 'temp')

	# SQLALCHEMY
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/demo?charset=utf8'
	DATABASE_CONNECT_OPTIONS = {'charset': 'utf8'}
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	# JWT
	JWT_AUTH_USERNAME_KEY = 'email'
	JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=60)
	JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=120)
	SECRET_KEY = ''

	REDIS_HOST = 'localhost'
	REDIS_PORT = 6379
	CELERY_BROKER_URL = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)
	CELERY_RESULT_BACKEND = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)

	# Google storage
	GC_STORAGE_PROJECT_NAME = ''
	GC_STORAGE_BUCKET = ''
	GC_STORAGE_FOLDER = ''
	GC_DEFAULT_FOLDER = ''
	MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # limit max length of request


class DevelopmentConfig(BaseConfig):
	SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/cryptosign?charset=utf8'


class StagingConfig(BaseConfig):
	BASE_URL = ''
	SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/cryptosign?charset=utf8'

	REDIS_HOST = ''
	REDIS_PORT = 6379
	REDIS_PASSWORD = ''
	CELERY_BROKER_URL = 'redis://:%s@%s:%s/0' % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT)
	CELERY_RESULT_BACKEND = 'redis://:%s@%s:%s/0' % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT)

	GC_STORAGE_PROJECT_NAME = ''
	GC_STORAGE_BUCKET = ''
	GC_STORAGE_FOLDER = ''
	GC_DEFAULT_FOLDER = ''

class ProductionConfig(BaseConfig):
	BASE_URL = ''
	SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/cryptosign?charset=utf8'

	REDIS_HOST = ''
	REDIS_PORT = 6379
	CELERY_BROKER_URL = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)
	CELERY_RESULT_BACKEND = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)

	GC_STORAGE_PROJECT_NAME = ''
	GC_STORAGE_BUCKET = ''
	GC_STORAGE_FOLDER = ''
	GC_DEFAULT_FOLDER = ''