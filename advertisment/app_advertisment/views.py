from django.shortcuts import render, redirect
from .models import Advertisment
from .forms import AdvertismentForm
from django.urls import reverse

def index( request ):
    advertisments = Advertisment.objects.all( )
    context = { 'advertisments' : advertisments }
    return render( request, 'index.html', context )

def top_sellers( request ):
    return render( request, 'top-sellers.html' )

def advertisment_post( request ):
    if request.method == 'POST':
        form = AdvertismentForm( request.POST, request.FILES )
        if form.is_valid( ):
            advertisment = Advertisment( **form.cleaned_data )
            advertisment.user = request.user
            advertisment.save( )
            url = reverse( 'main_page' )
            return redirect( url )
    else:
        form = AdvertismentForm( )
    context = { 'form' : form }
    return render( request, 'advertisment-post.html', context )

def register( request ):
    return render( request, 'register.html' )

def login( request ):
    return render( request, 'login.html' )

def profile( request ):
    return render( request, 'profile.html' )