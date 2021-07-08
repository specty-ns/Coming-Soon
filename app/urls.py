from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.ComingSoon,name="comingsoon"),
    path("teampage/",views.TeamPage,name="teampage"),

] 