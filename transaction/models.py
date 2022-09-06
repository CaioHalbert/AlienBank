from django.db import models
from django.conf import settings #para usar valores da aplicação auth
from account import models as mmodels


class transaction(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #modo de importar o id de usuário da auth
    accountId = models.ForeignKey(mmodels.account, on_delete=models.CASCADE) # Modo de usar o id da conta
    transactionType = models.IntegerField()
    transactionValue = models.FloatField()
    transactionTime = models.DateTimeField()
