from django.db import models
from django.conf import settings # para usar valores da aplicação auth

# Criamos o modelo de conta para vincular ao usuário
class account(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.FloatField()
