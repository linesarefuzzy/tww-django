from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.http import Http404, HttpResponseRedirect
from django.db import connection
# from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from loans.models import *

def home(request):
	return render_to_response('home.html')
	
def loans(request):
	loans = Loan.objects.filter(nivel__in=['Prestamo Activo','Prestamo Completo']).order_by('-signing_date')[:10]

	for l in loans:
		l.short_description = l.get_short_description(language_code='EN')
		l.description = l.get_description(language_code='EN')
		l.thumb_path = l.picture_paths()['thumb'] if l.picture_paths() else None
		
		# l.queries = connection.queries

	return render_to_response('loans/loans.html', {'loans': loans})
	
def loan_detail(request, loan_id):
	l = get_object_or_404(Loan, pk=loan_id)
	l.short_description = l.get_short_description(language_code='EN')
	l.description = l.get_description(language_code='EN')	
	l.picture_path = l.picture_paths()['large'] if l.picture_paths() else None
	return render_to_response('loans/loan_detail.html', {'loan': l})

@login_required
def user_profile(request):
	user_account = UserAccount.objects.get_or_create(user=request.user)[0]
	# users_loans = user_account.loans.all()
	user_loan_contributions = UserLoanContribution.objects.filter(user_account=user_account)
	users_loans = []
	for ulc in user_loan_contributions:
		users_loans.append((ulc, ulc.loan))
		# messages.debug(request, users_loans)
	return render(request, 'accounts/profile.html', 
		{'user': request.user, 'account': user_account, 'users_loans': users_loans})

def logout_view(request):
	logout(request)
	messages.success(request, 'You have been logged out.')
	return redirect('django.contrib.auth.views.login')

@login_required
def lend_form(request, loan_id):
	l = get_object_or_404(Loan, pk=loan_id)
	l.picture_path = l.picture_paths()['medium'] if l.picture_paths() else None
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
		# else:
		# 	if 'other_amount' not in form.errors:
		# 		form.errors['other_amount'] = form.errors['__all__']
	else:
		form = LendForm()
	
	return render(request, 'loans/lend_form.html', {'form': form, 'loan': l})
	# return render_to_response('loans/lend_form.html', {'loan': l})
