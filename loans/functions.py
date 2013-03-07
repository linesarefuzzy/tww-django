## Functions ##

import re, locale
from loans.models import *

def get_picture_paths(table_name, id, order_by=('priority','media_path')):
	try:
		image = Media.objects.filter(context_table=table_name, context_id=id).order_by(*order_by)[0]
	except IndexError:
		return {}
	# insert various things into file name
	thumb = re.sub(r'(\.[^.]+)$', r'.thumb\1', image.media_path)
	small = re.sub(r'(\.[^.]+)$', r'.small\1', image.media_path)
	medium = re.sub(r'(\.[^.]+)$', r'.medium\1', image.media_path)
	large = re.sub(r'(\.[^.]+)$', r'.large\1', image.media_path)
	return {
		'full':image.media_path, 
		'thumb':thumb,
		'small':small,
		'medium':medium,
		'large':large,
	}

def get_translation(table_name, column_name, id, language_code='EN'):
	translations = Translation.objects.filter(remote_table=table_name, remote_column_name=column_name, remote_id=id)
	if translations:
		try:
			content = translations.get(language__code=language_code).translated_content
		except Translation.DoesNotExist:
			content = translations.order_by('language__priority')[0].translated_content
		return content
	else: 
		# raise Translation.DoesNotExist
		return ''

def first_or_none(some_list):
	try: some_list[0]
	except IndexError: pass

# Format dollar amounts with commas and appropriate currency sign
def format_currency(amount, country):
	# insert commas
	#l.amount = format(l.amount, ',d') # doesn't work in python 2.5
	locale.setlocale(locale.LC_ALL, 'en_US')
	amount = locale.format('%d', amount, grouping=True)
	
	# currency sign
	currency = Currency.objects.get(country=country)
	symbol = re.sub('\$', ' $', currency.symbol) # add space before $ (pretty)
	amount = symbol + amount
	
	return amount

def get_project(obj):
	if obj.project_table.lower() == 'loans':
		try: return Loan.objects.get(id=obj.project_id)
		except Loan.DoesNotExist: pass
	elif obj.project_table.lower() == 'basicprojects':
		try: return BasicProject.objects.get(id=obj.project_id)
		except BasicProject.DoesNotExist: pass

