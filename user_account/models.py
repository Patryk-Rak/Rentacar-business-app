from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class AccountManager(BaseUserManager):

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
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
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

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Worker(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    payment = models.PositiveIntegerField(default=0)


class ClientProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=20, blank=True)
    state_region = models.CharField(max_length=30, blank=True)

    @receiver(post_save, sender=Account)
    def create_client_profile(sender, instance, created, **kwargs):
        if created:
            ClientProfile.objects.create(user=instance)

    @receiver(post_save, sender=Account)
    def save_client_profile(sender, instance, **kwargs):
        instance.clientprofile.save()
