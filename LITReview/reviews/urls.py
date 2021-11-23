from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ticket/create/', views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/', views.ticket_details, name='ticket_details'),
    path('ticket/<int:ticket_id>/edit/', views.edit_ticket, name='edit_ticket'),
    path('ticket/<int:ticket_id>/review/', views.create_review, name='create_review'),
    path('review/<int:review_id>/', views.review_details, name='review_details'),
    path('review/create/', views.create_ticket_and_review, name='create_ticket_and_review'),
    path('review/<int:review_id>/edit', views.edit_review, name='edit_review'),
    path('home/follow-users/', views.follow_users, name='follow_users')
]