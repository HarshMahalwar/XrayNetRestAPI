from django.urls import path
from .views import IndexView, BookDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='ex2'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
]