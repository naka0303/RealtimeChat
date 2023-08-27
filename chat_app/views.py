from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm, ChatroomCreationForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import resolve_url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser, ChatRoom, ChatRoomContent
from django import template
import json
from django.utils.safestring import mark_safe

from django.views import generic
from .forms import LoginForm
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

class UserUpdate(generic.UpdateView):
    model = CustomUser
    fields = ('username', 'icon')
    template_name = 'chat_app/user_update.html'
    
    def get_success_url(self):
        return resolve_url('chat_app:user_list')
    
class Login(LoginView):
    form_class = LoginForm
    template_name = 'chat_app/login.html'

class Logout(LogoutView):
    template_name = 'chat_app/top.html'

class MakeChatroom(generic.CreateView):
    form_class = ChatroomCreationForm
    template_name = 'chat_app/make_chatroom.html'

    def get_success_url(self):
        return resolve_url('chat_app:top')

class UserList(generic.ListView):
    template_name = 'chat_app/user_list.html'
    context_object_name = 'user_list'
    model = ChatRoom

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['chatroom_list'] = ChatRoom.objects.all
        return context

class ChatRoomList(generic.ListView):
    template_name = 'chat_app/chat_room.html'
    context_object_name = 'chat_room'
    model = CustomUser

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
           'chatroom_list': ChatRoom.objects.all(),
           'chatroom_content_list': ChatRoomContent.objects.filter(chatroom_no=self.kwargs['pk']),
           })
        return context
