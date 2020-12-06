from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main1'),
    path('health/', views.health, name='health')
]