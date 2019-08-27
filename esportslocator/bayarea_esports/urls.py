from django.urls import path
from . import views

urlpatterns = [
    #first paramater is blank because we are already in the directory
    #views.home is that function that we created in views.py and is also our homepage route and returns that http response when we request that homepage
    #name is the name for that path
    path('', views.home, name = 'bayarea-esports-home'),
    path('about/', views.about, name = 'bayarea-esports-about'),

]


