from django.contrib import admin

# Criamos uma instancia padrão de contas na app admin

from .models import account

admin.site.register(account)