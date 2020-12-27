from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # saves in database
            messages.success(request, f"Your message has been sent.Thanks for visiting our site!")
    else:
        form = ContactForm()

    obj = LandingPage.objects.all()
    objabout = About.objects.all()
    object_list = Team.objects.all()
    services = Services.objects.all()
    projects_web = Projects_web.objects.all()
    projects_loan = Projects_loan.objects.all()
    projects_webstartup = Projects_webstartup.objects.all()
    context = {
        'obj':obj,
        'objabout':objabout,
        'object_list':object_list,
        'services':services,
        'projects_web':projects_web,
        'projects_loan':projects_loan,
        'projects_webstartup':projects_webstartup,
        'form':form
    }

    return render(request,'teamtechs/index.html',context=context)



