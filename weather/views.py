from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def weather_now(request):
    return render(request, 'weather_now.html')
