from django.urls import path
from .views import answer

urlpatterns = [
    path( 'lesson_4', answer )
]