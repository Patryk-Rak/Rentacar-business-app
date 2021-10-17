from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate

from .models import Account, ClientProfile


class AccountRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True, help_text='Required')
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class ClientProfileForm(ModelForm):
    class Meta:
        model = ClientProfile
        fields = ('phone_number', 'address')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('email',)

# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#
# from .models import CustomUser
#
#
# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ('email', )
#
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('email', )
