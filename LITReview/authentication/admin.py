from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    """ Customization of the UserAdmin class in order to make it call a
    personalized form for the creation of a new user
    """
    pass


admin.site.register(User, CustomUserAdmin)
