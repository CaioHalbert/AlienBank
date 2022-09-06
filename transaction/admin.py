from django.contrib import admin

# Criamos uma instancia padrão de transações na app admin
from .models import transaction

admin.site.register(transaction)
