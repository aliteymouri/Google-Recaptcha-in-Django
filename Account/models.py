from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=120, unique=True)
    phone = models.CharField(max_length=11, unique=True, )
    fullname = models.CharField(max_length=80)
    image = models.ImageField(upload_to="users/profile", null=True, blank=True)
    bio = models.TextField(null=True, blank=True, )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'phone']

    def __str__(self):
        return F" User : {self.fullname}"

    @property
    def is_staff(self):
        return self.is_admin

