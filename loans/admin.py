from loans.models import *
from django.contrib import admin

class LoanAdmin(admin.ModelAdmin):
	list_display = ['cooperative','amount','signing_date','nivel']

# class UserAccount(admin.ModelAdmin):
# 	fields = ['balance']

admin.site.register(Loan, LoanAdmin)
admin.site.register(Cooperative)
admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(AccountClass)
admin.site.register(UserAccount)
