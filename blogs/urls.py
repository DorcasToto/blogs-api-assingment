from django.urls import path
from .views import BlogDetailView, BlogList


urlpatterns = [
    path('bloglist/', BlogList.as_view()),
    path('blogs/<int:pk>/', BlogDetailView.as_view())
]