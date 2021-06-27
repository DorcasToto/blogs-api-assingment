from django.urls import path
from .views import RegisterView, LoginView, BlogDetailView, BlogList


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('bloglist/', BlogList.as_view()),
    path('blogs/<int:pk>/', BlogDetailView.as_view())
]