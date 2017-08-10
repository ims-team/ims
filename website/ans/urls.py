from django.contrib.auth.views import login
from django.conf.urls import include, url
from django.contrib import admin
from ans.views import view_ansb
from ans.views import view_form
import os.path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
   #url(r'^admin/', admin.site.urls), 
     
 
   
   url(r'^view_home/',views.view_home, name='view_form'),
   url(r'^view_form/',views.view_form, name='view_form'),
   url(r'^view_ansb/',views.view_ansb, name='view_ansb'),     
   url(r'^$',views.view_form, name='view_form'),
   url(r'^$',views.view_ansb, name='view_ansb'),
   url(r'^$',views.view_home, name='view_home'),
   
   
] 
#if settings.DEBUG: 
 #    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
  #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
