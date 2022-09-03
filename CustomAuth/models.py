from django.db import models

#Customizamos a model ja existente na app authentication, adicionando ela como nossa model de user alem da authenticação

from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    pass
    # Aqui podemos adicionar novos campos

    def __str__(self):
        return self.username
