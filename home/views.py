from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"loggedIn" : False}
    if request.user.is_authenticated:
        context["loggedIn"] = True

    return render(request,"home.html", context)