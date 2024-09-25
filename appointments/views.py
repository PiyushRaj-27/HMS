from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from patients.models import patients
from staff.models import staff
from appointments.models import appointment
from datetime import datetime, timedelta
# Create your views here.

@login_required(login_url="/users/login")
def bookAppointment(request):
    user = request.user
    patient = patients.objects.get(email_id = user.id)

    deps = staff.objects.values("department").distinct()
    departments = []
    for item in deps:
        departments.append(item['department'])

    if request.method == "POST":
        pat = request.user
        dep = request.POST["department"]
        doc = staff.objects.get(department = dep)
        doct = doc.email
        date = datetime.today() + timedelta(days=1)
        date = str(date.date())
        time = datetime.today().time()
        time = str(time)
        if(int(patient.credit) >= 500):
            balance = int(patient.credit)
            balance -= 500
            patient.credit = str(balance)
            patient.save()
            appoint = appointment()
            appoint.pat = pat
            appoint.doc = doct
            appoint.department = dep
            appoint.date = date
            appoint.time = time
            appoint.save()
            return redirect("/users/dashboard")
        else:
            return HttpResponse("Insufficient balance!")

    context = {"user" : request.user, "dep": departments}
    return render(request, "bookAppointment.html", context)