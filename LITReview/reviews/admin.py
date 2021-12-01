from django.contrib import admin
from .models import Ticket, Review, UserFollow

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'has_review', 'id')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'user', 'ticket', 'id')

class UserFollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user', 'id')


# Register your models here.
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollow, UserFollowAdmin)