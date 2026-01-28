"""
URL configuration for proiectdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse
import pandas 
import requests as requests_module

def jokes_view(request, category):
    all_jokes_df =  pandas.read_csv("../jokes_cat.csv", index_col=0)
    return HttpResponse(f" {all_jokes_df.loc[category] [0]}")

def chuck_view(request):
    return HttpResponse("Aici va fi ceva despre CHUCK NORRIS...")

def random_joke_view(request):
    module_response =  requests_module.get("https://api.chucknorris.io/jokes/random")
    joke = module_response.json()["value"]
    return HttpResponse(joke) 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('glume/<category>/', jokes_view),
    path('chuck/', chuck_view),


    path('', random_joke_view)

]
