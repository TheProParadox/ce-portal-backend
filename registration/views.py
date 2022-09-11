from django.shortcuts import render

# Create your views here.

def Team(request):
    return render(request, 'form/team.html')
