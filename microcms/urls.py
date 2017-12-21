"""microcms URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from news.views import index,article_detail,column_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', column_detail, name='column'),
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$',article_detail, name='article'),
]
