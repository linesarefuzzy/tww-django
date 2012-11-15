import re, locale
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import Http404
from django.db import connection
# from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from loans.models import *

def home(request):
	return render_to_response('home.html')
	
def loans(request):
	loans = Loan.objects.filter(nivel__in=['Prestamo Activo','Prestamo Completo']).order_by('-signing_date')[:20]

	for l in loans:
		l.short_description = l.get_short_description(language_code='EN')
		l.description = l.get_description(language_code='EN')
		
		# insert commas into dollar amounts
		#l.amount = format(l.amount, ',d') # doesn't work in python 2.5
		locale.setlocale(locale.LC_ALL, 'en_US')
		l.amount = 'AR$' + locale.format('%d', l.amount, grouping=True)
		
		l.queries = connection.queries

	return render_to_response('loans/loans.html', {'loans': loans})
	
def loan_detail(request, loan_id):
	l = get_object_or_404(Loan, pk=loan_id)
	l.short_description = l.get_short_description(language_code='EN')
	l.description = l.get_description(language_code='EN')
	return render_to_response('loans/loan_detail.html', {'loan': l})

@login_required
def user_profile(request):
	user_account = UserAccount.objects.get_or_create(user=request.user)
	return render_to_response('accounts/profile.html', {'user': request.user, 'account': user_account})

def logout_view(request):
	logout(request)
	return redirect('/accounts/login?message=loggedOut')
	# return render_to_response('registration/login.html', {'message': "You have been logged out."})
