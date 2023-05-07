from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUser(AbstractUser, UserManager):

    email = models.EmailField(verbose_name="メールアドレス", unique=True, blank=False, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password1', 'password2']

    def __str__(self):
        return self.email
