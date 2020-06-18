from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.home),
    url(r',home/', views.home),
    url(r'get_count/', views.get_count, name='get_count'),
    url(r'get_count2/', views.get_count2, name='get_count2'),
]