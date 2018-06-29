"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView
from rango import views
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request,user):
        return '/rango/'
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^accounts/register/',MyRegistrationView.as_view(),name='registration_register'),
]
# if settings.DEBUG:
#     urlpatterns += ['django.views.static',[r'media/(?P<path>.*)','serve',{'document_root':settings.MEDIA_ROOT}],]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_PATH)