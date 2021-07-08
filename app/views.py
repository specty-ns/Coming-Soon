from django.shortcuts import render

def ComingSoon(request):
    return render(request,"app/index.html")

def TeamPage(request):
    return render(request,"app/team.html")

# Create your views here.
