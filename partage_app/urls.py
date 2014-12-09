from django.conf.urls import url
import  django_cas.views
from partage_app import views 

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^categories$', views.index,  {"sort": "category"}, name='index'),
    url(r'^lieux$', views.index,  {"sort": "location"}, name='index'),
    url(r'^ajouter$', views.add, name="add"),
    url(r'^enlever$', views.remove, name="remove"),
    url(r'^editer/(?P<obj_id>\d+)$', views.edit, name="edit"),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/login/login/$', 'django_cas.views.login', name='login'),
    url(r'^accounts/login/$', 'django_cas.views.login', name='login'),
    url(r'^accounts/logout/$', 'django_cas.views.logout', name='logout'),
]

