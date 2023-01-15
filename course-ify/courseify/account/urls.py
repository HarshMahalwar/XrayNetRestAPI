from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from .views import *
from . import views
from .forms import (UserLoginForm)

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('register/', AccountRegister.as_view(), name='register'),

    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('profile/edit/', EditDetails.as_view(), name='edit_details'),
    path('profile/delete_user/', DeleteUser.as_view(), name='delete_user'),
 ]