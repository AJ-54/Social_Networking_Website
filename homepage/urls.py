from django.conf.urls import url , include
from django.contrib import admin
from .import views as homepage_views

from . import views

urlpatterns = [url(r'^$', views.index),
               url(r'^Signup/', views.signup, name='register'),
               url(r'^About/', views.about),
               url(r'^Signin/',views.signup),
               url(r'^account_activation_sent/$', homepage_views.account_activation_sent, name='account_activation_sent'),
               url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
               homepage_views.activate, name='activate'),
               ]