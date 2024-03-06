"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.urls import path
from home.views import *
from vege.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.conf import settings
from django.conf.urls.static import static




#from firstproject.home.views import success_page, contact, about, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/',about),
    path('contact/',contact),
    path('success_page/',success_page),
    path('admin',admin.site.urls),
    path('receipes/',receipes),
    path('delete-receipe/<id>/',delete_receipe),
    path('update-receipe/<id>/',update_receipe),
    path('login/',login_page),
    path('register/',register),
    path('logout/',logout_page)


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
