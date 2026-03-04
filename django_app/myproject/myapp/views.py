from django.http import HttpResponse
from django.shortcuts import render
from .models import Message

def home(request):
    return HttpResponse("Hello from Django!")

def greet(request, name):
    return render(request, "greet.html", {"name": name})

def message_list(request):
    messages = Message.objects.all()
    return render(request, "messages.html", {"messages": messages})