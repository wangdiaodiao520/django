from django.conf.urls import url
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^login/', login),
    url(r'^complaints/', complaints),
    url(r'^download/', download),
    url(r'^logout/', logout),]
