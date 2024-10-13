from django.urls import path
from . import views


urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name= 'update'),
    path('user/', views.UserListCreate.as_view(), name='user'),
    path('user/<int:pk>/', views.UserRetrieveUpdateDestroy.as_view(), name= 'update-user'),
    
]

