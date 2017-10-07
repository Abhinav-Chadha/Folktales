from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', AboutView.as_view()),]