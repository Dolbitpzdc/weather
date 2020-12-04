import pyowm

owm = pyowm.OWM("c6cfc1ad754846160c1e039cbda0e774")

mgr = owm.weather_manager()

place = input('Input sity ')['place']

observation = mgr.weather_at_place(place)

w = observation.weather

temp=w.temperature('celsius')['temp']

print("In sity  " + place + ' now ' + str(temp))
