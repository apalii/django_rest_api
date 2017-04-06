"""rest_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="rest_app/home.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^github_webhook/$', 'rest_app.views.github_webhook'),
]

# Django auth
urlpatterns += [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
]

# Monitor
urlpatterns += [
    url(r'^monitor/', include("rest_app.urls", namespace='monitor')),
]

# API
urlpatterns += [
    url(r'^api/v0/', include("rest_app.api.urls", namespace='rest-api')),
]
