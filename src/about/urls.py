from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^about/$', views.AboutView.as_view(), name='about'),

    url(r'^getinvolved/$', views.GetInvolvedView.as_view(), name='getinvolved'),

    url(r'^team/$', views.TeamView.as_view(), name='team'),

    url(r'^work/$', views.WorkView.as_view(), name='work'),

    url(r'^gaa/$', views.GAAView.as_view(), name='gaa'),


]

