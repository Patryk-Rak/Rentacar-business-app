from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings
import os
from django.utils.translation import ugettext_lazy as _


class AccountManager(BaseUserManager):
#    use_in_migrations = True

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(max_length=60, null=False, blank=False, default='Empty')
    last_name = models.CharField(max_length=60, null=False, blank=False, default='Empty')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Worker(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    payment = models.PositiveIntegerField(default=0)


class ClientProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email
