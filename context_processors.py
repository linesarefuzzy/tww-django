# from django.conf import settings # import the settings file
import tww

def settings_processor(request):
	# d = {}
	# for key in dir(settings):
	# 	if not key.startswith('__'):
	# 		d[key] = getattr(settings, key)
	# return d
	return {'settings':tww.settings.__dict__}