from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .utils import generate_id
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken



class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, default=generate_id(), max_length=64)
    profile_pic = models.ImageField(upload_to='media/', null=True, blank=True)
    email = models.EmailField(_("email address"), unique=True, db_index=True)
    username = models.CharField(max_length=64, unique=True)
    phone_no = models.CharField(max_length=15, blank=False, null=False)
    sex = models.CharField(max_length=30, blank=False, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
