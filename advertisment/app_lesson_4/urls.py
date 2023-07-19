from django.urls import path
from .views import answer

urlpatterns = [
    path( '', answer )
]