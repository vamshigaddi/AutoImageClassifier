# images app urls.py

from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.home, name='home'),  # Map the root path to a 'home' view
    path('check-status/', views.check_status, name='check_status'),
    path('upload/', views.upload_images, name='upload_images'),  # URL pattern for image upload
    path('login/', views.login_view, name='login_view'),
    #path('signup/',views.signup,name='signup')
]


