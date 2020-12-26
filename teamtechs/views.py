from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from .models import *

# Create your views here.


def home(request):
    obj = LandingPage.objects.all()
    objabout = About.objects.all()
    object_list = Team.objects.all()
    context = {
        'obj':obj,
        'objabout':objabout,
        'object_list':object_list
    }
    return render(request,'teamtechs/index.html',context=context)
