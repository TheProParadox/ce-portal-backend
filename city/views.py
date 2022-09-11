from django.shortcuts import render
from .models import Applicant, City , Competition, Team
from django.shortcuts import render
from .forms import EntryForm
from django.http import HttpResponseRedirect

def landing(request) :
    context = {
        'cities': City.objects.all(),
    }
    return render(request, 'city/landing.html',context)

def dashboard(request,pk) :
    city = City.objects.get(pk=pk)
    data = {
        'city' : city,
        'competitions': city.cityCompetitions.all(),
    }
    return render(request, 'city/dashboard.html',data)

def teamForm(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        data = request.POST
        for i in range( int(data.get('number'))):
            # print(data.get('city'),data.get('competition'))
            applicant = Applicant(name = data.get('name' + str(i)), email = data.get('email' + str(i)), city = data.get('city'), competition = data.get('competition'))
            applicant.save()
            # print('success' + str(i))
        team = Team(name = data.get('name'),)
        print(data)
        # team.save()
        return render(request, 'form/success.html', {'form': form})

    # if a GET (or any other method) we'll create a blank for
    else:
        form = EntryForm()
        return render(request, 'form/team.html',{'form': form})
# Create your views here.
