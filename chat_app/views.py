from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import resolve_url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser
from django import template
import json
from django.utils.safestring import mark_safe

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
    template_name = 'chat_app/signup.html'

    def get_success_url(self):
        return resolve_url('chat_app:user_list')
    
class Login(LoginView):
    template_name = 'chat_app/login.html'

class Logout(LogoutView):
    template_name = 'chat_app/top.html'

class UserList(generic.ListView):
    template_name = 'chat_app/user_list.html'
    context_object_name = 'user_list'
    model = CustomUser

class ChatRoom(generic.ListView):
    template_name = 'chat_app/chat_room.html'
    context_object_name = 'chat_room'
    model = CustomUser

"""
class ChatPage(generic.DetailView):
    template_name = 'chat_app/chat.html'
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # pkを指定してデータを絞り込む
        data_list = CustomUser.objects.filter(id=self.kwargs['pk']).values()
        context['customuser_data_list'] = data_list

        return context
"""
