from django.urls import path
from .views import TesteView

urlpatterns = [
    path('teste/', TesteView.as_view(), name='teste'),  
]