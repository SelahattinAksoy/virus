"""adenovirus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from  virus.views import index
from  virus.views import team
from  virus.views import predicter
from  virus.views import virustable
from  virus.views import about
from  virus.views import virustableintro
from  virus.views import ppintro
from  virus.views import viral_infectintro
from  virus.views import ppipredicter
from  virus.views import viral_infectpredicter
from  virus.views import publications
from  virus.views import announcement


admin.site.site_header="Welcome to MSKU VIRAL"
#admin.site.site_title="Welcome to MSKU Viral"
#admin.site.index_title="MSKU VIRAL ADMIN"



urlpatterns = [
     path('admin/', admin.site.urls),
     path('', index),
     path('team/', team),
     path('predicter_1/', predicter),
     path('virustable/', virustable, name="virustable"),
     #path('virustable/', virustable),
     path('about/', about),
     path('virustableintro/', virustableintro),
     path('ppintro/', ppintro),
     path('viral_infectintro/', viral_infectintro),
     path('ppipredicter/', ppipredicter),
     path('viral_infectpredicter/', viral_infectpredicter,name="viral_infectpredicter"),
     path('publications/', publications),
     path('announcement/', announcement),
     
     
     
]
