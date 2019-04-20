from django.contrib import admin  
from django.urls import path  
from djangoapp import views  
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
urlpatterns = [  
    url(r'^admin/', admin.site.urls),  
    url(r'^hello/', views.hello),
	url(r'^$',views.login),
    url(r'^show/', views.show),
    url(r'^mail/', views.mail),
]  
if settings.DEBUG:
   urlpatterns += [
      url(r'^media/(?P<path>.*)$',
	  serve,{'document_root':
	         settings.MEDIA_ROOT,}),]