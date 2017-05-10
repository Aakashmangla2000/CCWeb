from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from mysite.core import views as core_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import views


urlpatterns = [
   url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^$', core_views.home, name='home'),
      url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^members/$', views.MmebersPageView.as_view(), name='members'),
         url(r'^blog/$', views.SponsorsPageView.as_view(), name='blog'),
    url(r'^compguide/$', views.CompGuidePageView.as_view(), name='compguide'),
url(r'^competitions/$', views.CompetitionsPageView.as_view(), name='competitions'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
]

urlpatterns += staticfiles_urlpatterns()