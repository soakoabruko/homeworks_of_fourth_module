from django.shortcuts import render
from .models import Advertisment

def index( request ):
    advertisments = Advertisment.objects.all( )
    context = { 'advertisments': advertisments }
    return render( request, 'index.html', context )

def top_sellers( request ):
    return render( request, 'top-sellers.html' )

def advertisment_post( request ):
    return render( request, 'advertisment-post.html' )

def register( request ):
    return render( request, 'register.html' )

def login( request ):
    return render( request, 'login.html' )

def profile( request ):
    return render( request, 'profile.html' )