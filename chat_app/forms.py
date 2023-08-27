from typing import Any
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ChatRoom
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for filed in self.fields.values():
            filed.widget.attrs['class'] = 'form-control'
            filed.widget.attrs['placeholder'] = filed.label

class ChatroomCreationForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ('chatroom_no', 'chatroom_name')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for filed in self.fields.values():
            filed.widget.attrs['class'] = 'form-control'
            filed.widget.attrs['placeholder'] = filed.label
