from django.contrib import admin
from .models import Entry
from .models import City
from .models import Competition

admin.site.register(Entry)
admin.site.register(City)
admin.site.register(Competition)
# Register your models here.
