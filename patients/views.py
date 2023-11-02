from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import patients
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import string
#dummy data      email: test2@gmail.com      pass: test.123123

# Create your views here.
def authenticateName(fname: str, lname: str) -> bool:
    if fname.isalpha() and lname.isalpha():
        return True
    else:
        return False

def matchPass(pass1: str, pass2: str) -> bool:
    return pass1 == pass2

def authenticatePass(password: str) -> bool:
    alpha = string.ascii_letters
    digits = string.digits
    special = [".", "_", "-", "?","@"]
    if len(password)>=8:
        alphaFlag = False
        digitFlag = False
        specialFlag = False
        for i in password:
            if i in alpha:
                alphaFlag = True
            if i in digits:
                digitFlag = True
            if i in special:
                specialFlag = True
        return alphaFlag and digitFlag and specialFlag
    else:
        return False

def register(request):
    context = {"isRegistered" : False, "passErr": False, "invalidPass": False, "invalidName": False, "emailRegistered": False}
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        state = request.POST["state"]
        city = request.POST["city"]
        pincode = request.POST["pincode"]
        address = request.POST["address"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        marraige = request.POST["martial"]
        empl = request.POST["empl"]
        img = request.FILES["pic"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        blood = request.POST["blood"]
        age = request.POST["age"]
        namecheck = authenticateName(fname= fname, lname= lname)
        if namecheck:
            passcheck = authenticatePass(pass1)
            if passcheck:
                passauth = matchPass(pass1=pass1, pass2 = pass2)
                if passauth:
                    try:
                        User.objects.get(username = email)
                        context["emailRegistered"] = True
                    except ObjectDoesNotExist:
                        u1 = User.objects.create(username = email)
                        u1.set_password(pass1)
                        u1.save()
                        p1 = patients()
                        p1.fname = fname
                        p1.lname = lname
                        p1.state = state
                        p1.city = city
                        p1.pincode = pincode
                        p1.address = address
                        p1.phone = phone
                        p1.email = u1
                        p1.empl = empl
                        p1.marr = marraige
                        p1.age = age
                        p1.bloodGrp = blood
                        p1.img = img
                        p1.save()
                        context["isRegistered"] = True
                else:
                    context["passErr"] = True
            else:
                context["invalidPass"] = True
            
        else:
            context["invalidName"] = True

    
    return render(request,"registerPatient.html", context=context)


def loginuser(request):
    context = {"loggedIn": False, "invalid": False}
    if request.user.is_authenticated:
        context["loggedIn"] = True
    
    if request.method == "POST":
        print("Trying to log in")
        email = request.POST["uname"]
        password = request.POST["pass"]
        user = authenticate(username=email, password=password)
        if user is not None:
            print("logged in")
            login(request, user)
            context["loggedIn"] = True
            return redirect("/users/dashboard")
        else:
            context["invalid"] = True
    return render(request, "login.html", context= context)

@login_required(login_url="/users/login")
def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")

@login_required(login_url="/users/login")
def dashboard(request):
    userid = request.user.id
    patient = patients.objects.get(email_id = userid)
    imgUrl = patient.img.url

    context = {"fname": patient.fname, "lname":patient.lname, "img": imgUrl, "state": patient.state, "city": patient.city, "pincode": patient.pincode, "email": request.user.username, "marriage":patient.marr, "empl": patient.empl.capitalize(), "age":patient.age, "Blood":patient.bloodGrp} 
    return render(request,"patientDashBoard.html", context)


@login_required(login_url="/users/login")
def update(request):
    userid = request.user.id
    patient = patients.objects.get(email_id = userid)
    context = {"invalidName": False}
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        state = request.POST["state"]
        city = request.POST["city"]
        pincode = request.POST["pincode"]
        address = request.POST["address"]
        phone = request.POST["phone"]
        marraige = request.POST["martial"]
        empl = request.POST["empl"]
        blood = request.POST["blood"]
        age = request.POST["age"]
        namecheck = authenticateName(fname= fname, lname= lname)
        if namecheck:
            patient.fname = fname
            patient.lname = lname
            patient.state = state
            patient.city = city
            patient.pincode = pincode
            patient.address = address
            patient.phone = phone
            patient.marr = marraige
            patient.empl = empl
            patient.age = age
            patient.bloodGrp = blood
            patient.save()
            return redirect("/users/dashboard")
        else:
            context["invalidName"] = True
    return render(request, "patientUpdateDetail.html", context)