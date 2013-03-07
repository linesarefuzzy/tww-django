from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.http import Http404, HttpResponseRedirect
# from django.db import connection
# from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from loans.models import *
from loans.forms import *

def home(request):
	return render(request, 'home.html')
	
def loans(request):
	loans = Loan.objects.filter(nivel__in=['Prestamo Activo','Prestamo Completo']).order_by('-signing_date')[:10]

	for l in loans:
		l.short_description = l.get_short_description(language_code='EN')
		l.description = l.get_description(language_code='EN')
		l.thumb_path = l.picture_paths().get('thumb')
		# l.queries = connection.queries

	return render(request, 'loans/loans.html', {'loans': loans})
	
def loan_detail(request, loan_id):
	l = get_object_or_404(Loan, pk=loan_id)
	l.short_description = l.get_short_description(language_code='EN')
	l.description = l.get_description(language_code='EN')	
	l.picture_path = l.picture_paths().get('medium')
	l.pasos = []
	for paso in l.get_pasos():
		# if paso.finalized > 0: paso.finished_un = 'finished'
		# else: paso.finished_un = 'unfinished'
		if paso.completed: paso.is_completed = 'completed'
		else: paso.is_completed = 'not_completed'
		paso.summary = paso.get_translation('Summary', language_code='EN') or paso.summary
		paso.details = paso.get_translation('Details', language_code='EN') or paso.details
		paso.logs = []
		for log in paso.projectlog_set.all():
			log.explanation = log.get_translation('Explanation', language_code='EN')
			log.detailed_explanation = log.get_translation('DetailedExplanation', language_code='EN')
			paso.logs.append(log)
		l.pasos.append(paso)
	return render(request, 'loans/loan_detail.html', {'loan': l})

@login_required
def user_profile(request):
	user_account = UserAccount.objects.get_or_create(user=request.user)[0]
	# users_loans = user_account.loans.all()
	
	user_loan_contributions = UserLoanContribution.objects.filter(user_account=user_account)
	users_loans = []
	for ulc in user_loan_contributions:
		ulc.loan.thumb_path = ulc.loan.picture_paths().get('thumb')
		users_loans.append((ulc, ulc.loan))
	
	return render(request, 'accounts/profile.html', 
		{'user': request.user, 'account': user_account, 'users_loans': users_loans})

def logout_view(request):
	logout(request)
	messages.success(request, 'You have been logged out.')
	return redirect('loans.views.login_view')

# from django.dispatch import receiver
# from django.contrib.auth.signals import user_logged_in
# @receiver(user_logged_in)
# def myreceiver(sender, **kwargs):
# 	messages.debug(kwargs['request'], kwargs['user'].username+' logged in')

def login_view(request):
	''' Contains both a login form and a new user registration form. '''
	
	# Login form
	if request.method == 'POST' and request.POST['submit'] == 'Login': # If the login form has been submitted
		lform = LoginForm(request.POST)
		if lform.is_valid():
			d = lform.cleaned_data
			user = authenticate(username=d['username'], password=d['password'])
			login(request, user)
			return redirect('loans.views.user_profile')
	else:
		lform = LoginForm()

	# New user registration form
	if request.method == 'POST' and request.POST['submit'] == 'Sign Up': # If the new user form has been submitted
		newform = NewUserForm(request.POST)
		if newform.is_valid():
			d = newform.cleaned_data
			user = User.objects.create_user(
				d['username'],
				d['email'],
				d['password1']
			)
			# user = newform.save(commit=False)
			user.first_name = d['first_name']
			user.last_name = d['last_name']
			# user.email = d['email']
			user.save()
			user = authenticate(username=d['username'], password=d['password1'])
			login(request, user)
			# messages.debug(request, u.__dict__)
			return redirect('loans.views.user_profile')
	else:
		newform = NewUserForm()
	
	# Render page with both forms
	return render(request, 'accounts/login.html', {'newform': newform, 'lform': lform})

@login_required
def lend_form(request, loan_id):
	l = get_object_or_404(Loan, pk=loan_id)
	l.picture_path = l.picture_paths().get('medium')
	if request.method == 'POST': # If the form has been submitted...
		form = LendForm(request.POST)
		if form.is_valid(): # All validation rules pass
			amount = form.cleaned_data['amount']
			other_amount = form.cleaned_data['other_amount']
			if amount == 0:
				amount = other_amount
			u = UserAccount.objects.get(user=request.user)
			c = UserLoanContribution(
				user_account = u,
				loan = l,
				amount = amount,
				balance = amount,
			)
			c.save()
			u.balance -= amount
			u.save()
			messages.success(request, 'Thank you! Your loan has been made.')
			return redirect('loans.views.user_profile') # Redirect after POST
	else:
		form = LendForm()
	
	return render(request, 'loans/lend_form.html', {'form': form, 'loan': l})
