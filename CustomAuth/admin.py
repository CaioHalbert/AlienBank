from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

'''
Criamos uma separação na aplicação admin para que possamos gerenciar nossos usuários e suas permissões
'''

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]
    
admin.site.register(CustomUser, CustomUserAdmin)