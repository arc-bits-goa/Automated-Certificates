from django.conf.urls import include, url
from django.contrib import admin
from tools import user
urlpatterns = [
	url(r'^create-users/', user.index, name='user'),
    url(r'^', admin.site.urls),
    url(r'^', include('main.urls')),
]
