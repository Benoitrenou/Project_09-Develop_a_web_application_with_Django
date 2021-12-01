from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import UserFollow

from . import models

User = get_user_model()


class TicketForm(forms.ModelForm):
    """ Form for Ticket creation
    """
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        """ Override of Meta class
        """
        model = models.Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Couverture'
            }


class DeleteTicketForm(forms.Form):
    """ Form for Ticket suppression
    """
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    """ Form for Review creation
    """
    choices = [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    rating = forms.TypedChoiceField(
        label='Note',
        widget=forms.RadioSelect(),
        choices=choices,
        coerce=int
        )

    class Meta:
        """ Override of Meta class
        """
        model = models.Review
        fields = ['headline', 'rating', 'body']
        labels = {
            'headline': 'Titre',
            'body': 'Description',
            'rating': 'Note'
            }


class DeleteReviewForm(forms.Form):
    """ Form for Review suppression
    """
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class UserFollowForm(forms.ModelForm):
    """ Form for UserFollow creation
    """
    def __init__(self, user, *args, **kwargs):
        """ Override of __init__ to receive the user at the call
        """
        self.user = user
        super().__init__(*args, **kwargs)

    followed_user = forms.CharField(
        max_length=63,
        label='Utilisateur recherché'
        )

    class Meta:
        """ Override of Meta class
        """
        model = UserFollow
        fields = ['followed_user']

    def clean_followed_user(self):
        """ Validation of field followed_user
        """
        username = self.cleaned_data['followed_user']
        try:
            user = User.objects.get(username=username)
            if self.user == user:
                raise ValidationError(
                    'Vous ne pouvez pas vous suivre vous-mêmes'
                    )
            if user in self.user.get_connections():
                raise ValidationError('Vous suivez déjà cet utilisateur')
        except User.DoesNotExist:
            raise ValidationError('Utilisateur inconnu !')
        return user

    def save(self, commit=True):
        """ Create and save new instance of UserFollow -
        Return this instance
        """
        user_follows = UserFollow(
            user=self.user,
            followed_user=self.cleaned_data['followed_user']
        )
        if commit:
            user_follows.save()
        return user_follows


class DeleteFollowForm(forms.Form):
    """ Form for UserFollow suppression
    """
    delete_follow = forms.BooleanField(widget=forms.HiddenInput, initial=True)
