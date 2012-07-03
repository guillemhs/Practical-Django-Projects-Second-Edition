from django.conf.urls import patterns, url
from cms.cab.views.home import home

urlpatterns = patterns('',
    url(r'^$', home, name='cab_home'),
)
