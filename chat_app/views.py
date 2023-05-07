from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import resolve_url
from django.contrib.auth import login

from django.views import generic
# from .forms import (
#     LoginForm, UserCreateForm, UserUpdateForm, MyPasswordChangeForm,
#     MyPasswordResetForm, MySetPasswordForm, EmailChangeForm
# )

# Create your views here.

class Top(generic.TemplateView):
    template_name = 'chat_app/top.html'

class SignUp(generic.CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('chat_app:top')
    template_name = 'chat_app/signup.html'

    def get_success_url(self):
        return resolve_url('chat_app:top')
