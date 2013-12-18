from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from jqmapp import views

urlpatterns = patterns('',
    (r'^asd/', TemplateView.as_view(template_name="jqmapp/layout.html")),
    url(r'^demo1/$', views.Demo1View.as_view(), name='demo1'),
)