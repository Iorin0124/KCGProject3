import os
import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
	'default' : {
		'ENGINE' : 'django.db.backends.mysql',
		'NAME' : 'djangodb',
		'USERS' : 'root',
		'PASSWORD' : 'root'
		'HOST' : '',
		'PORT' : '',
	}
}

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
