from django.shortcuts import render
from .models import Data

def home(request):
    return render(request, "index.html")
