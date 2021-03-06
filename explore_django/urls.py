"""learning_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views, settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^courses/', include('courses.urls', namespace='courses2')),
    re_path(r'^suggest/$', views.suggestion_view, name='suggestion'),
    re_path(r'^$', views.homepage, name='home'),

]


urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
    re_path(r'^__debug__/', include(debug_toolbar.urls)),
]
