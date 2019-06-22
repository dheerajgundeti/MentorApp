from django.contrib import messages
from django.views import View
from onlineapp.models import *
from django.shortcuts import *
from onlineapp.forms import *
from django.urls import resolve
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


def my_first_view(request):
    return HttpResponse("my first response.\n")
