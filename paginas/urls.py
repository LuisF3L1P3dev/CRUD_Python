from django.urls import path
from .views import TesteView, SobreView,PrincipalView 

urlpatterns = [
    path('teste/', TesteView.as_view(), name='teste'),  
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('principal/', PrincipalView.as_view(), name='principal'),
]