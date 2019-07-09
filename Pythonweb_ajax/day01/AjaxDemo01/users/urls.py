from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/',views.register),
    url(r'^is-name/$',views.is_name),
    url(r'^createuser$',views.createuser),
    url(r'^query/$',views.query_users),
    url(r'^query_server/$',views.query_server),
    url(r'^jso/$',views.jso),
    url(r'^json/$',views.json_views),
    url(r'^json_server/$',views.json_server),
    url(r'^user_server/$',views.user_server),
    url(r'^front_json/$',views.front_json),
    url(r'^front_server/$',views.front_server),

]