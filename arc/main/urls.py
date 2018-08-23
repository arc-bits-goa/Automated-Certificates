from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'printg/(?P<id>\d+)/$',views.printGraduating, name="Graduating"),
    url(r'printt/(?P<id>\d+)/$',views.printThesis, name="Thesis"),
	
]