# coding: utf-8
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from m3.actions.urls import get_app_urlpatterns
import wsfactory.urls

urlpatterns = []

urlpatterns += staticfiles_urlpatterns()
urlpatterns += get_app_urlpatterns()
urlpatterns += wsfactory.urls.urlpatterns
