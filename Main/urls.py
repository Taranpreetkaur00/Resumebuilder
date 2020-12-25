from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' , views.home , name='home'),
    url(r'^contact/$' , views.contact , name='contact'),
    url(r'^resume/$' , views.resume , name='resume'),
    url(r'^services/$' , views.services , name='services'),
    url(r'^about/$' , views.about , name='about'),
    url(r'^resume/single/$' , views.resumesingle , name='resumesingle'),
    url(r'^panel/$' , views.panel , name='panel'),
    url(r'^login/$' , views.my_login , name='my_login'),
    url(r'^logout/$' , views.my_logout , name='my_logout'),
    url(r'^answer/comments/(?P<pk>\d+)/$' , views.answer_cm , name='answer_cm'),
    
   
]