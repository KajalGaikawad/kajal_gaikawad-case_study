from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('track/', views.track_service_requests, name='track_service_requests'),
]
