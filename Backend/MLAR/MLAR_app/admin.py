from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(First_License_Application)
admin.site.register(Renew_last_license)
admin.site.register(Regain_lost_license)
admin.site.register(Employee)
admin.site.register(Validate)

