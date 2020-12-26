from django.contrib import admin
from .models import *


admin.site.site_header = 'TeamTechKenya'
#admin.site.site_title =  ''

admin.site.register(LandingPage)
admin.site.register(About)
admin.site.register(Team)