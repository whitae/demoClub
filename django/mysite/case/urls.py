from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.case_title, name="case_title")
]