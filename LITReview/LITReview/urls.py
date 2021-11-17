"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

import authentication.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('change-password/', authentication.views.change_password, name='password_change'),
    path('change-paswword/done/', authentication.views.change_password_done, name='password_change_done'),
    path('logout/', authentication.views.logout_page, name='logout'),
    path('home/', reviews.views.home, name='home'),
    path('ticket/create/', reviews.views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/', reviews.views.view_ticket, name='view_ticket'),
    path('ticket/<int:ticket_id>/edit/', reviews.views.update_ticket, name='edit_ticket'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)