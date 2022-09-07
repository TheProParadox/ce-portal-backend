from django.contrib import admin
from persons.models import City, Competition,Person

admin.site.register(Competition)
admin.site.register(City)
admin.site.register(Person)
