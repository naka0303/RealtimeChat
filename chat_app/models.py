from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUser(AbstractUser, UserManager):
    email = models.EmailField(verbose_name="メールアドレス", unique=True, blank=False, null=False)
    icon = models.ImageField(upload_to='icon', default='icon/no_image.png')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password1', 'password2']

    def __str__(self):
        return self.email

class ChatRoom(models.Model):
    chatroom_no = models.IntegerField(default=0)
    chatroom_name = models.CharField(max_length=20, default=None)

class ChatRoomContent(models.Model):
    chatroom_no = models.IntegerField(default=0)
    username = models.CharField(max_length=10)
    icon = models.ImageField(upload_to='icon/', default='icon/no_image.png')
    message = models.CharField(max_length=100)
    register_datetime = models.DateTimeField(help_text='投稿日時')
