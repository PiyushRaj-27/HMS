from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from patients.models import patients
from appointments.models import appointment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import string
import datetime
# Create your views here.
@login_required(login_url="/users/login")
def payment(request):
    if (request.user.is_authenticated):
        if request.method == "POST":
            user = request.user
            patient = patients.objects.get(email_id = user.id)
            cardholder = request.POST["name"]
            cardnum = request.POST["cardnumber"]
            cvv = request.POST["cvv"]
            amount = request.POST["amount"]
            if len(cvv) == 3 and int(amount)>0 and len(cardnum) == 12:
                balance = int(patient.credit)
                balance+= int(amount)
                patient.credit = str(balance)
                patient.save()
                return redirect("/users/dashboard")
            else:
                return HttpResponse("Invalid card or amount!")
        return render(request, "payment.html")
    else:
        return redirect("/")