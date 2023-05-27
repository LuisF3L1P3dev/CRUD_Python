from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import CarroViewsSet

routs = DefaultRouter()
routs.register('carros', CarroViewsSet ) 

urlpatterns = [
    path('', include(routs.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
