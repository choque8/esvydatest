from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    # Examples:
    # url(r'^$', 'esvyda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('apps.users.urls')),

    url(r'^',login,  {'template_name':'login.html'}, name='logins'),
]