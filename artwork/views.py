from django.shortcuts import render
from django.http import HttpResponse
from .models import Artwork, Home, Profile, Contact


def index(request):
    homes = Home.objects.all()
    return render(request, 'index.html', {'homes': homes, 'cur': 'homes'})


def artwork(request):
    artworks = Artwork.objects.all()
    return render(request, 'artwork.html', {'artworks': artworks, 'cur': 'artwork'})


def profile(request):
    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles, 'cur': 'profile'})


def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contacts, 'cur': 'contact'})




