from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def register(request):
    return render(request, 'register.html', {})

def schedule(request):
    return render(request, 'schedule.html', {})

def speakers(request):
    return render(request, 'speakers.html', {})

def venue(request):
    return render(request, 'venue.html', {})
