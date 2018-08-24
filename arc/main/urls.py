from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'printg/(?P<id>\d+)/$',views.printGraduating, name="Graduating"),
    url(r'printt/(?P<id>\d+)/$',views.printThesis, name="Thesis"),
    url(r'printc/(?P<id>\d+)/$',views.printCGPA, name="CGPA"),
    url(r'printcc/(?P<id>\d+)/$',views.printCompletion, name="Completion"),


	
]