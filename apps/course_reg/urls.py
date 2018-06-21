from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^process$', views.process, name="process"),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]