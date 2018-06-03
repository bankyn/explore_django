from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.course_list, name='list'),
    re_path(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.course_detail,
            name='step'),
    re_path(r'(?P<pk>\d+)/$', views.course_detail, name='detail')
]


