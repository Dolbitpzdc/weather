from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# def getStatic(request):
#     print(request)
#     return render(request, 'home.html')
