from django.shortcuts import render

def IndexView(request):
    #Página Web
    return render(request, "index.html")

# Create your views here.
