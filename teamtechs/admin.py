from django.contrib import admin
from .models import *


admin.site.site_header = 'TeamTechKenya'
#admin.site.site_title =  ''

admin.site.register(LandingPage)
admin.site.register(Team)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Contact)
admin.site.register(Projects_web)
admin.site.register(Projects_loan)
admin.site.register(Projects_webstartup)
