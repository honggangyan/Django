from django.shortcuts import render
from django.http import HttpResponse

# When a particular url is visited, it will return this message.
# Configure the url in this hello app

#def index(request):
    #return HttpResponse("Hello, world!")

def honggang(request):
    return HttpResponse("Hello, Honggang!")

# A custom route
#def greet(request, name):
   # return HttpResponse(f"Hello, {name.capitalize()}!")

def index(request):
    return render(request, "hello/index.html")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })