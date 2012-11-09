from django.conf.urls.defaults import *
# from django.views.generic import DetailView, ListView
# from loans.models import Loan

urlpatterns = patterns('loans.views',
	# url(r'^loans/$',
	#	  ListView.as_view(
	#		  queryset = Loan.objects.all().order_by('-signing_date')[:20],
	#		  context_object_name='loans',
	#		  template_name = 'loans/loans.html')),
	# url(r'^loans/(?P<pk>\d+)/$',
	#	  DetailView.as_view(
	#		  model = Loan,
	#		  template_name = 'loans/loan_detail.html')),
		
	(r'^$', 'loans'),
	(r'^(?P<loan_id>\d+)/$', 'loan_detail'),
)

urlpatterns += patterns('users.views',
	(r'^$', 'users'),
	(r'^(?P<username>\w+)/$', 'user_profile'),
)