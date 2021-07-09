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
from django.urls import path
from core import views as core_views


from django.conf import settings

urlpatterns = [
      path('',core_views.product_list, name='product-list'),
      path('',core_views.pc_list, name='product-list'),
      path('',core_views.celular_list, name='product-list'),
      path('',core_views.Ri_list, name='product-list'),

      path('product-new/', core_views.product_new, name='product-new'),
      path('product-newPc/', core_views.product_newPc, name='product-newPc'),
      path('product-newcelular/', core_views.product_newcelular, name='product-newcelular'),
      path('product-newRi/', core_views.product_newRi, name='product-newRi'),

      path('product-update/ <idProducto>', core_views.product_update, name='product-update'),
      path('product-update/ <idProductoPc>', core_views.product_updatePc, name='product-updatePc'),
      path('product-update/ <idProductocelular>', core_views.product_updatecelular, name='product-updatePc'),
      path('product-update/ <idProductoRi>', core_views.product_updateRi, name='product-updatePc'),

      path('product-delete/<idProducto>',core_views.product_delete,name='product-delete'),
      path('product-delete/<idProductoPc>',core_views.product_deletePc,name='product-deletePc'),
      path('product-delete/<idProductocelular>',core_views.product_deletecelular,name='product-deletecelular'),
      path('product-delete/<idProductoRi>',core_views.product_deleteRi,name='product-deleteRi'),
      
     
 
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
