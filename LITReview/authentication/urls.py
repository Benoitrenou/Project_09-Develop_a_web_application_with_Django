from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.signup_page, name='signup'),
    path('change-password/', views.change_password, name='password_change'),
    path('change-paswword/done/', views.change_password_done, name='password_change_done'),
    path('logout/', views.logout_page, name='logout')
]