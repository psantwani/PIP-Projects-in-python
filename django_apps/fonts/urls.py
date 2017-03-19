from django.conf.urls import url

from . import views

app_name = 'fonts'
urlpatterns = [
    url(r'^$', views.index),
]
