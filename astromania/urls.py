from django.urls import path
from .import views

urlpatterns=[path('home',views.homepage),path('login',views.login),path('log_ch',views.log_check),path('reg',views.reg),path('register',views.register),path('about',views.about),path('contact',views.contact),path('recipes',views.recipes),path('Tandoori',views.Tandoori),]
