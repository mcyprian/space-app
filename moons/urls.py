from django.urls import path
from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='moon-list', permanent=False), name='index'),
    url(r'^api/moons/$', views.MoonList.as_view(), name='moon-list'),
    url(r'^api/moons/(?P<pk>[0-9]+)$', views.MoonDetail.as_view(), name='moon-detail'),
]
