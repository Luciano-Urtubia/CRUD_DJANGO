
from django.urls import path , include
from .views import ProductoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Producto',ProductoViewSet )



urlpatterns = [
    
    path('api/',include(router.urls)),
  


]
