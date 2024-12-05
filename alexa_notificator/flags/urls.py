from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.flags_dashboard, name='flags_dashboard'),
    # If you have additional views, add them here
]