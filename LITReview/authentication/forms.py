from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    """ Form for a user to signup
    """
    class Meta(UserCreationForm.Meta):
        """ Override of Meta class
        """
        model = get_user_model()
        fields = ('username', )


class LoginForm(forms.Form):
    """ Form for a user to login
    """
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(
        max_length=63,
        widget=forms.PasswordInput,
        label='Mot de passe'
        )
