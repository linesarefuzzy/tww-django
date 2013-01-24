from settings_base import *

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'tww_labase',					   # Or path to database file if using sqlite3.
		'USER': 'tww_django',					   # Not used with sqlite3.
		'PASSWORD': '',					 # Not used with sqlite3.
		'HOST': '',					  # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',						 # Set to empty string for default. Not used with sqlite3.
	}
}
