from django.urls import path,include
from .import views
from teamtechs.views import *



urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
	path('accounts/',include('django.contrib.auth.urls')),
	path('codewithteamtechkenya/',views.codewithttk,name='codewithttk'),
	path('learningsessions/',views.registerwithttk,name='registerwithttk'),
]
