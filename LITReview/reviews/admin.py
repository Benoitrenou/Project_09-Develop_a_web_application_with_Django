from django.contrib import admin
from .models import Ticket, Review, UserFollow

class TicketAdmin(admin.ModelAdmin):
    """ Handle model Ticket representation in admin interface
    """
    list_display = ('title', 'author', 'has_review', 'id')

class ReviewAdmin(admin.ModelAdmin):
    """ Handle model Review representation in admin interface
    """
    list_display = ('headline', 'user', 'ticket', 'id')

class UserFollowAdmin(admin.ModelAdmin):
    """ Handle model UserFollow representation in admin interface
    """
    list_display = ('user', 'followed_user', 'id')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollow, UserFollowAdmin)
