from django.contrib import admin
from .models import City , Competition, Applicant, Team

# Register your models here.
admin.site.register(City)
admin.site.register(Competition)
admin.site.register(Applicant)
admin.site.register(Team)