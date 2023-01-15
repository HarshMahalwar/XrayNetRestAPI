from django.urls import path
from .views import FileViewSet

urlpatterns = [
    path('', FileViewSet.as_view({'get': 'list'}), name='file-upload'),
]