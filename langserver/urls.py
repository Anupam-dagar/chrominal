from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/c/$', views.compilec, name='compilec'),
    url(r'^api/cpp/$', views.compilecpp, name='compilecpp'),    
]