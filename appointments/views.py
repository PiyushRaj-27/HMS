from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from staff.models import staff
from appointments.models import appointment
from datetime import datetime, timedelta
# Create your views here.

@login_required(login_url="/users/login")
def bookAppointment(request):
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
        appoint = appointment()
        appoint.pat = pat
        appoint.doc = doct
        appoint.department = dep
        appoint.date = date
        appoint.time = time
        appoint.save()
        return redirect("/users/dashboard")

    context = {"user" : request.user, "dep": departments}
    return render(request, "bookAppointment.html", context)