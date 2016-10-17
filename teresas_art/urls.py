"""defines URL patterns for app"""

from django.conf.urls import url, include

from . import views

urlpatterns = [
	#homepage
	url(r'^$', views.index, name='index'),
	url(r'^recent/$', views.recent, name='recent'),
	url(r'^works/$', views.works, name='works'),
	url(r'^cv/$', views.cv, name='cv'),
	url(r'^about/$', views.about, name='about'),
]