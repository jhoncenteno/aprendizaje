from django.shortcuts import render
from AppMarketing.models import Signup

# Create your views here.

def home(request):
    if request.method == "POST":
        email =request.POST["email"]
        nueva_suscripcion = Signup()
        nueva_suscripcion.email = email
        nueva_suscripcion.save()

    return render(request, '1home.html')