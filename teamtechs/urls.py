from django.urls import path
from .import views
from teamtechs.views import *



urlpatterns = [
    path('',views.home,name='home'),
]