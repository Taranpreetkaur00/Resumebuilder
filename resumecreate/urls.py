from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^personal/submit/$', views.personal_add , name= 'personal_add'  ),
    url(r'^education/submit/(?P<pk>\d+)/$', views.education_add , name= 'education_add'  )
]