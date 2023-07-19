from django.urls import path
from .views import index, top_sellers, advertisment_post, register, login, profile

urlpatterns = [
    path( '', index, name = 'main_page' ),
    path( 'top-sellers/', top_sellers, name = 'top_sellers' ),
    path( 'advertisment-post/', advertisment_post , name = 'advertisment_post' ),
    path( 'register/', register, name = 'register' ),
    path( 'login/', login, name = 'login' ),
    path( 'profile/', profile, name = 'profile' )
]