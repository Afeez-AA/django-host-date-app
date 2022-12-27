

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
import socket

def index(request):
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    hostname = socket.gethostname()
    return HttpResponse(f"Current date: {current_date}<br>Hostname: {hostname}")
from django.shortcuts import render
from django.http import HttpResponse
import datetime
import socket

def index(request):
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    hostname = socket.gethostname()
    return HttpResponse(f"Current date: {current_date}<br>Hostname: {hostname}")

