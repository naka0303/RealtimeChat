from django.shortcuts import render

from django.views import generic
# from .forms import (
#     LoginForm, UserCreateForm, UserUpdateForm, MyPasswordChangeForm,
#     MyPasswordResetForm, MySetPasswordForm, EmailChangeForm
# )

# Create your views here.

class Top(generic.TemplateView):
    template_name = 'chat_app/top.html'
