from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'), 
    path('room/', views.room, name='room'),  # Map root URL to the room view
     # Map /lobby/ URL to the lobby view
    # ... Other URLs
]