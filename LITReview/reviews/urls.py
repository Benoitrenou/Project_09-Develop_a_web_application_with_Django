from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/posts/', views.personal_posts, name='personal_posts'),
    path('ticket/create/', views.CreateTicketView.as_view(), name='create_ticket'),
    path('ticket/<pk>/', views.TicketDetailsView.as_view(), name='ticket_details'),
    path('ticket/<pk>/edit/', views.UpdateTicketView.as_view(), name='edit_ticket'),
    path('ticket/<int:ticket_id>/review/', views.create_review, name='create_review'),
    path('review/<int:review_id>/', views.review_details, name='review_details'),
    path('review/create/', views.create_ticket_and_review, name='create_ticket_and_review'),
    path('review/<int:review_id>/edit', views.edit_review, name='edit_review'),
    path('home/follow-users/', views.follow_users, name='follow_users')
]