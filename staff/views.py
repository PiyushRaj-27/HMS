from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import string
from .models import staff
# Create your views here.
# dummy data      username : dranup@gmail.com     password: dranup.123123

def loginUser(request):
    context = {"invalid": False, "loggedIn": False}
    if request.user.is_authenticated:
        User = request.user
        isStaff = User.is_staff
        if isStaff == 1:
            context["loggedIn"] = True


    if request.method == "POST":
        email = request.POST["uname"]
        password = request.POST["pass"]
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request,user)
            context["loggedIn"] = True
            return redirect("/staff/dashboard")
        else:
            context["invalid"] = True
    return render(request,"staffLogin.html", context)

@login_required(login_url="/staff/login")
def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")

@login_required(login_url="staff/login")
def dashboard(request):
    User = request.user
    UserId = request.user.id
    Staff = staff.objects.get(email_id = UserId)
    imgUrl = Staff.img.url
    context = {"fname": Staff.fname, "lname": Staff.lname,"department": Staff.department.capitalize() ,"level": Staff.level.capitalize(), "age" : Staff.age, "blood": Staff.bloodGrp, "state": Staff.state, "city": Staff.city, "address": Staff.address, "img": imgUrl, "email": User.username}

    return render(request,"staffDashBoard.html", context)

def staffList(request):
    Users = User.objects.filter(is_staff = 1)
    context = {"admins": [], "doctors": []}
    for item in Users:
        if item.is_superuser == 1:
            context["admins"].append(item)
        else:
            doctor = staff.objects.get(email_id = item.id)
            context["doctors"].append(doctor)
    return render(request, "staffList.html", context)