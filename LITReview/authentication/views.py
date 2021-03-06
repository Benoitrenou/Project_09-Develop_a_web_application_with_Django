from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

from . import forms


def signup_page(request):
    """ Generates the view to signup
    """
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(
        request,
        'authentication/signup.html',
        context={'form': form}
        )


def login_page(request):
    """ Generates the view to login
    """
    if request.user.is_authenticated:
        return redirect('home')
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
    return render(
        request,
        'authentication/login.html',
        context={'form': form, 'message': message}
        )


@login_required
def change_password(request):
    """ Generates a view for user to change passsword
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request,
                'Your password was successfully updated!'
                )
            return redirect('password_change_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(
        request,
        'authentication/password_change_form.html',
        {'form': form}
        )


@login_required
def change_password_done(request):
    """ Generates view confirming password change
    """
    return render(request, 'authentication/password_change_done.html')


def logout_page(request):
    """ Generates view confirming logout
    """
    logout(request)
    return render(request, 'authentication/logout.html')
