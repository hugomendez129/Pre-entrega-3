"""
URL configuration for Pre_entrega_3 project.

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
from WEB.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    #inicio de la web
    path('',inicio, name="inicio"),

    #buscador de cada producto
    path('calzado/',Buscar_calzado, name="Buscar_calzado"),
    path('indumentaria/',Buscar_indumentaria, name="Buscar_indumentaria"),
    path('accesorios/',Buscar_accesorios, name="Buscar_accesorios"),
    path('carga/',fullcarga),
    
    

]
