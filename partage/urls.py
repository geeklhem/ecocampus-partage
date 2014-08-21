from django.conf.urls import patterns, url,include
import  django_cas.views
from django.contrib import admin
from partage_app import views 

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^categories$', views.index,  {"sort": "category"}, name='index'),
    url(r'^lieux$', views.index,  {"sort": "location"}, name='index'),
    url(r'^ajouter$', views.add, name="add"),
    url(r'^enlever$', views.remove, name="remove"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django_cas.views.login'),
    url(r'^accounts/logout/$', 'django_cas.views.logout'),
)
