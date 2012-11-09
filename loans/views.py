import re, locale
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.db import connection
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from loans.models import Loan, Media, UserAccount

# Media.objects.get(context_table="'Loans'", context_id=799)
# print Media.objects.all().order_by('context_id')

def home(request):
	return render_to_response('home.html')
	
def loans(request):
	loans = Loan.objects.filter( Q(nivel='Prestamo Activo') | Q(nivel='Prestamo Completo') ).order_by('-signing_date')[:20]

	for l in loans:
		# images
		try:
			l.image = Media.objects.filter(context_table='Loans', context_id=l.id).order_by('-priority')[0]
		except IndexError:
			try:
				l.image = Media.objects.filter(context_table='Cooperatives', context_id=l.cooperative.id).order_by('-priority')[0]
			except IndexError:
				l.image = None
		# insert ".thumb" into image path
		if l.image:
			l.image.media_path = re.sub(r'(\.[^.]+)$', r'.thumb\1', l.image.media_path)
		
		# insert commas into dollar amounts
		#l.amount = format(l.amount, ',d') # doesn't work in python 2.5
		locale.setlocale(locale.LC_ALL, 'en_US')
		l.amount = 'AR$' + locale.format('%d', l.amount, grouping=True)
		
		# descriptions from translations table
		# l.description = l.short_description #or l.short_description_english or l.description
		
		l.queries = connection.queries

	return render_to_response('loans/loans.html', {'loans': loans})
	
def loan_detail(request, loan_id):
	loan = get_object_or_404(Loan, pk=loan_id)
	return render_to_response('loans/loan_detail.html', {'loan': loan})

@login_required
def user_profile(request):
	try:
		user_account = UserAccount.objects.get(user=request.user)
	except UserAccount.DoesNotExist:
		# create UserAccount record if it doesn't exist for this user
		pass # ...
	return render_to_response('users/user_profile.html', {'user': request.user, 'account': user_account})
	