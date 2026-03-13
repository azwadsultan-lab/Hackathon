# myapp/views.py
from django.shortcuts import render

def home_view(request):
    # This tells Django to find and display your home.html file
    return render(request, 'home.html')