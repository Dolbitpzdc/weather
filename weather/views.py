from django.shortcuts import render
import pyowm

def home(request):
    return render(request, 'home.html')

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
