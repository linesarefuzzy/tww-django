from loans.models import *
from django.contrib import admin

# class UserAccount(admin.ModelAdmin):
# 	fields = ['balance']

class LoanAdmin(admin.ModelAdmin):
	list_display = ['cooperative','amount','signing_date','nivel']
admin.site.register(Loan, LoanAdmin)

class TodoAdmin(admin.ModelAdmin):
	list_display = ['description','point_person','second','status','modified']
admin.site.register(Todo, TodoAdmin)

class UserLoanContributionInline(admin.TabularInline):
	model = UserLoanContribution
	extra = 0
class UserAccountAdmin(admin.ModelAdmin):
	inlines = (UserLoanContributionInline,)
admin.site.register(UserAccount, UserAccountAdmin)

admin.site.register(Cooperative)
admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(AccountClass)
admin.site.register(Translation)
admin.site.register(Language)
# admin.site.register(UserLoanContribution)
