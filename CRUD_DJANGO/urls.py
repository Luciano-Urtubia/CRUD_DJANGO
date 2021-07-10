"""CRUD_DJANGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path , include 
from core import views as core_views







from django.conf import settings

urlpatterns = [
      path('',core_views.product_list, name='product-list'),
    

      path('product-new/', core_views.product_new, name='product-new'),


      path('lista_2/', core_views.lista2__, name='lista_2'),
      path('lista_3/', core_views.lista3__, name='lista_3'),
      path('lista_4/', core_views.lista4__, name='lista_4'),
      path('listaf2/', core_views.listaf2__, name='listaf2'), 
      path('listaf3/', core_views.listaf3__, name='listaf3'), 
      path('product-update/ <idProducto>', core_views.product_update, name='product-update'),
      path('product-delete/<idProducto>',core_views.product_delete,name='product-delete'),

  




      
     
 
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
