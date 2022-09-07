from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import EntryForm
from .models import City,Competition
# Create your views here.
def create(request):
    submitted=False
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/entry?submitted=True')
    else:
        form = EntryForm
        if 'submitted'in request.GET:
           submitted=True
        
    return render(request, 'entry.html', {'form' : form,'submitted':submitted})

def load_cities(request):
    city_id = request.GET.get('city')
    Competition = Competition.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'success.html', {'competion': Competition})


