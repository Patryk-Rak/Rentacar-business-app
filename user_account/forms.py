from django import forms
from django.contrib.auth.forms import UserCreationForm
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


class AccountEditForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'hide_email' )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def save(self, commit=True):
        account = super(AccountEditForm, self).save(commit=False)
        account.email = self.cleaned_data['email'].lower()
        account.first_name = self.cleaned_data['first_name']
        account.last_name = self.cleaned_data['last_name']
        account.hide_email = self.cleaned_data['hide_email']
        if commit:
            account.save()
        return account
