"""
URL configuration for lerningDjango project.

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
from django.urls import path

from app1.views import index_page, user_login, user_logout, forkids_page, discount_page, user_reg, product, addToCart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index_page, name='index'),
    path('forkids/', forkids_page, name='forkids_page'),
    path('discount/', discount_page, name='discount_page'),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('reg/', user_reg, name='reg'),
    path('product/', product, name='product'),
    path('addToCart/', addToCart, name='addToCart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
