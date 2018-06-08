from django.urls import path
from django.views.generic.base import TemplateView
from .models import Disease, Symptom
from . import views
urlpatterns = [
    path('drmas/', views.Home.as_view(), name='home'),
	path('', views.Home.as_view(), name='home'),
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('diagnose/', views.Diagnose.as_view(), name='diagnose'),
	path('predict/', views.Predict.as_view(), name='predict'),
]