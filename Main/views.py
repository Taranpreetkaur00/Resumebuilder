from django.shortcuts import render , get_object_or_404,redirect  #404 for ,when we dont have database can we can handle it without showing 404
from .models import Main
# Create your views here.

def home (request):
    site = Main.objects.get(pk=1)
    return render(request,'index.html',{'site':site})

def contact(request):
    site = Main.objects.get(pk=1)
    return render(request,'contact.html',{'site':site})