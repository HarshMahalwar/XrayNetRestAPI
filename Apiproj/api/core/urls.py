from django.urls import path
from core import views
from django.urls import re_path as url

urlpatterns = [
    url("",views.ResultApiView.as_view())
]
