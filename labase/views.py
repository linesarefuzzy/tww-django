from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from labase.models import Loan

def loans(request):
    loans = Loan.objects.all().order_by('-signing_date')[:10]
    return render_to_response('loans/index.html', {'loans': loans})
    
def loan_detail(request, loan_id):
    l = get_object_or_404(Loan, pk=loan_id)
    return render_to_response('loans/loan_detail.html', {'loan': l})