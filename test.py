import django
from loans.models import *

l = Loan.objects.get(id=878)
print l.__dict__.keys()
# print l.__class__.verbose_name

# pasos = l.pasos
# p = pasos[0]
# 
# for p in pasos: 
# 	# print ProjectLog.objects.filter(paso=p)
# 	for log in p.projectlog_set.all():
# 		print log


# from django import forms
# from django.contrib.auth.forms import *
# 
# class MyForm(UserCreationForm):
# 	first_name = forms.CharField()
# 
# print MyForm()


