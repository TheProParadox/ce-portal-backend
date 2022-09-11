from django.urls import path
from . import views

urlpatterns = [
    path('TeamReg', views.Team, name = 'team-reg')
]