from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.member_posts, name='member_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]