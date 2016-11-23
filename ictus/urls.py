from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    #url(r'^$', views.study_list),
    url (r'^$', views.patient_list),
    url (r'^patient/new/$', views.view_patient, name ='new_patient'),
    url (r'^patient/(?P<patient_pk>[0-9]+)/$', views.view_patient, name ='view_patient'),
    url (r'^episode/(?P<episode_pk>[0-9]+)/$', views.view_episode, name ='view_episode'),
    url (r'^patient/(?P<patient_pk>[0-9]+)/new_episode/$', views.new_episode, name ='view_patient'),
    url (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
]
