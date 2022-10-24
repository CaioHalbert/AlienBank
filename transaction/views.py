from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from .models import transaction
from django.shortcuts import render

# Create your views here.
@login_required
def getAllTransactions(request):
    objUser = request.user.id
    transactions = transaction.objects.filter(userId = objUser)

    return HttpResponse(transactions[0].transactionTime)

    

    