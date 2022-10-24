from django import forms

from .models import transaction

class CreateTransactionForm(transaction):

    class Meta:
        model = transaction
        fields = (
            "userId",
            "accountId",
            "transactionType",
            "transactionValue",
            "transactionTime"
         )

