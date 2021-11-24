from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from .models import UserFollow

from . import models

User = get_user_model()

class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']

class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['rating', 'headline', 'body']

class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class UserFollowForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        """Modifier l'initialisation pour recevoir l'utilisateur à l'instanciation
        du formulaire.
        """
        self.user = user
        super().__init__(*args, **kwargs)

    followed_user = forms.CharField(max_length=63, label='Utilisateur recherché')
    
    class Meta:
        model = UserFollow
        fields = ['followed_user']

    def clean_followed_user(self):
        """Validation du champ followed_user
        avec récupération de l'utilisateur en base.
        """
        username = self.cleaned_data['followed_user']
        try:
            user = User.objects.get(username=username)
            if self.user == user:
                raise ValidationError('Vous ne pouvez pas vous suivre vous-mêmes')
            user_connections = self.user.get_connections()
            if user in self.user.get_connections():
                raise ValidationError('Vous suivez déjà cet utilisateur')
        except User.DoesNotExist:
            raise ValidationError('Utilisateur inconnu !')
        return user

    def save(self, commit=True):
        """Crée et sauvegarde une nouvelle instance de subscriber.
        """
        user_follows = UserFollow(
            user=self.user,
            followed_user=self.cleaned_data['followed_user']
        )
        if commit:
                user_follows.save()
        return user_follows

class DeleteFollowForm(forms.Form):
    delete_follow = forms.BooleanField(widget=forms.HiddenInput, initial=True)