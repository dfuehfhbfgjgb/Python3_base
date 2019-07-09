from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^load/$',views.load_views),
    url(r'^01-server/$',views.server01),
    url(r'^02-get/$',views.get_views),
    url(r'^02-server/$',views.server02),
    url(r'^03-post/$',views.post_views),
    url(r'^03-server/$',views.server03),
    url(r'^04-ajax/$',views.ajax_views),
    url(r'^04-server/$',views.server04),
    url(r'^05-cross/$',views.cross_views),
    url(r'^05-server/$',views.server05),
    url(r'06-js/$',views.js_views),
    url(r'^06-server/$',views.server06),
]