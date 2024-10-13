
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_api.urls')),
    #path('api/users/', ListUsers.as_view()),
    #path('api/token/auth/', CustomAuthToken.as_view())
]
