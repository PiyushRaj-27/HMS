from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import report
from patients.models import patients
from staff.models import staff
from appointments.models import appointment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import string
import datetime
import mimetype
import os
# Create your views here.

@login_required(login_url="/users/login")
def showReport(request):
    user = request.user
    userid = user.id
    print(userid)
    reportsList = report.objects.filter(pat_id = userid)

    context = {"reports": reportsList}
    return render(request, "patientReports.html", context=context)


@login_required(login_url="/users/login")
def downloadReport(request, filename):
    fl_path = "D:/College Files/Sem5/Assignment/HMLS/hms/media/data/reports"
    fl_path += "/" + filename
    if os.path.exists(fl_path):
        with open(fl_path, "rb") as f:
            response = HttpResponse(f.read(), content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(fl_path)
            return response
    else:
        return HttpResponse("File not found")

