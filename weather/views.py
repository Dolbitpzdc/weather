from django.shortcuts import render
from django.http import JsonResponse
import pyowm

def home(request):
    if request.GET.get("city"):
        owm = pyowm.OWM("c6cfc1ad754846160c1e039cbda0e774")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(request.GET.get("city"))
        w = observation.weather
        temp=w.temperature('celsius')['temp']

        return render(request, 'home.html', {"city":  request.GET.get("city"), "response": "In city  " + str(request.GET.get("city")) + ' now ' + str(temp),})
    else:
        return render(request, 'home.html', {"city":  request.GET.get("city") ,"response": ""})

def weather_now(request):
    if request.GET.get("city"):
        owm = pyowm.OWM("c6cfc1ad754846160c1e039cbda0e774")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(request.GET.get("city"))
        w = observation.weather
        temp=w.temperature('celsius')['temp']

        return render(request, 'weather_now.html', {"response": "In sity  " + str(request.GET.get("city")) + ' now ' + str(temp),})
    else:
        return render(request, 'weather_now.html', {"response": ""})

def getWeather(request):
    if request.GET.get("city"):
        try:
            owm = pyowm.OWM("c6cfc1ad754846160c1e039cbda0e774")
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(request.GET.get("city"))
            w = observation.weather
            temp=w.temperature('celsius')['temp']
        except:
            return JsonResponse({"error": "Your city not found."})

        return JsonResponse({"temperature": temp})
    else:
        return JsonResponse({"error": "Your city not found."})
