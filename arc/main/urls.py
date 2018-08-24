from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'printg/(?P<id>\d+)/$',views.printGraduating, name="Graduating"),
    url(r'printt/(?P<id>\d+)/$',views.printThesis, name="Thesis"),
    url(r'printc/(?P<id>\d+)/$',views.printCGPA, name="CGPA"),
    url(r'printcc/(?P<id>\d+)/$',views.printCompletion, name="Completion"),
    url(r'printe/(?P<id>\d+)/$',views.printEnglish, name="English"),
    url(r'printfc/(?P<id>\d+)/$',views.printContinuing, name="Continuing"),
    url(r'printfg/(?P<id>\d+)/$',views.printGraduated, name="Graduated"),
    url(r'printts/(?P<id>\d+)/$',views.printSem, name="Thesissem"),
	]