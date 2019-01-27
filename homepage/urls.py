from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.index),
               url(r'^About/', views.about),
               url(r'^Signup/', views.signup),
               url(r'^Signin/', views.signin),
               ]