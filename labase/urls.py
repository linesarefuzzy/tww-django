from django.conf.urls.defaults import *
# from django.views.generic import DetailView, ListView
from labase.models import Loan

urlpatterns = patterns('labase.views',
    # url(r'^loans/$',
    #     ListView.as_view(
    #         queryset = Loan.objects.all().order_by('-signing_date')[:20],
    #         context_object_name='loans',
    #         template_name = 'loans/loans.html')),
    # url(r'^loans/(?P<pk>\d+)/$',
    #     DetailView.as_view(
    #         model = Loan,
    #         template_name = 'loans/loan_detail.html')),
		
    (r'^$', 'loans'),
    (r'^(?P<loan_id>\d+)/$', 'loan_detail'),
)