from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    creation_form = CustomUserCreationForm
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)