from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.db import connection
from labase.models import Loan, Media

# Media.objects.get(context_table="'Loans'", context_id=799)
# print Media.objects.all().order_by('context_id')


def loans(request):
    loans = Loan.objects.all().order_by('-signing_date')[:20]
    for l in loans:
        try:
            l.image = Media.objects.filter(context_table='Loans', context_id=l.id)[0]
        except IndexError:
            try:
                l.image = Media.objects.filter(context_table='Cooperatives', context_id=l.cooperative.id)[0]
            except IndexError:
                pass
        
        # l.image = images
        l.queries = connection.queries
    return render_to_response('loans/index.html', {'loans': loans})
    
def loan_detail(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)
    return render_to_response('loans/loan_detail.html', {'loan': loan})