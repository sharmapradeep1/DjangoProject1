"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from first_app import views ########## Pattern 1 STEP 10 Manage url in project - Import views from the app
from django.conf.urls import include ########## Pattern 2 STEP 10 Manage urls in app, include apps url script here


urlpatterns = [
    url(r'^home1/',views.home1,name='home1'), ########## Pattern 1 STEP 20 Manage url in project - if http://127.0.0.1:8000/home, invoke home function in app - views
    url(r'^first_app/',include('first_app.urls')), ########## Pattern 2 STEP 20 Manage url in app - if http://127.0.0.1:8000/first_app, navigate to urls in first_app
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', views.user_logout, name='logout'),
]
