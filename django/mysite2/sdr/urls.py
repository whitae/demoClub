from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^select$', views.sdr_select, name="sdr_select"),
]