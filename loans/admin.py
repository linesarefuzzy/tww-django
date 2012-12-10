from loans.models import *
from django.contrib import admin

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
admin.site.register(Account, list_display=['name','type'])
admin.site.register(AccountClass) #, list_display=['name','super_class'])
admin.site.register(Language)
admin.site.register(Division)

class ProjectLogInline(admin.TabularInline):
	model = ProjectLog
	extra = 0
class ProjectEventAdmin(admin.ModelAdmin):
	inlines = [ProjectLogInline]
admin.site.register(ProjectEvent, ProjectEventAdmin)

admin.site.register(Member)
admin.site.register(Blog)
