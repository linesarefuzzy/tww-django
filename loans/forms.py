## Forms ##

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from loans.models import *

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput())
	
	def clean(self):
		data = super(LoginForm, self).clean()
		username = data.get('username')
		password = data.get('password')
		
		# Check if username exists
		try: 
			User.objects.get(username=username)
		except User.DoesNotExist: 
			raise forms.ValidationError("Username not found.")
			return data
		
		# Check password
		u = authenticate(username=username, password=password)
		if not u:
			raise forms.ValidationError("Incorrect password.")
		# elif not u.is_active():
		# 	raise forms.ValidationError("Sorry, this account is disabled.")
		
		return data

# class NewUserForm(UserCreationForm):
class NewUserForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'

	username = forms.CharField(max_length=30)
	first_name = forms.CharField()
	last_name = forms.CharField()
	password1 = forms.CharField(max_length=30, widget=forms.PasswordInput()) #render_value=False
	password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(), label='Re-enter password')
	email = forms.EmailField()

	def clean_username(self): # check username not already taken
		try:
			User.objects.get(username=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError("This username has been taken. Please choose another.")
	
	def clean(self): # check if passwords match
		d = super(NewUserForm, self).clean()
		if 'password1' in d and 'password2' in d: #check that both passed first validation
			if d['password1'] != d['password2']: # check if they match each other
				raise forms.ValidationError("Passwords do not match")
		return d

class LendForm(forms.Form):
	AMOUNT_CHOICES = (
		(25, '$25'),
		(50, '$50'),
		(100, '$100'),
		(0, 'Other amount'),
	)
	amount = forms.DecimalField(widget=forms.Select(
		choices=AMOUNT_CHOICES, 
		attrs={'onchange':'show_hide_other()'}))
	# amount = forms.TypedChoiceField(choices=AMOUNT_CHOICES, coerce='decimal')
	other_amount = forms.DecimalField(max_digits=12, decimal_places=2, required=False)

	def clean(self):
		cleaned_data = super(LendForm, self).clean()
		amount = cleaned_data.get('amount')
		other_amount = cleaned_data.get('other_amount')

		if amount == 0 and not other_amount:
			# raise forms.ValidationError('Please enter an amount in the "Other amount" field.')
			if not 'other_amount' in self._errors:
				self._errors['other_amount'] = self.error_class([u'Please enter an amount in the "Other amount" field.'])
			if 'other_amount' in cleaned_data: 
				del cleaned_data['other_amount']

		# Always return the full collection of cleaned data.
		return cleaned_data
