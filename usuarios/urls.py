from django.urls import include, path
""" from rest_framework.routers import DefaultRouter
from projectCar import settings
from .views import CarroViewsSet, home, form, create, view, edit, update, delete, teste
from django.conf.urls.static import static
from django.conf import settings """
from django.contrib.auth import views as auth_views
from .views import us
urlpatterns = [
   path('login/', auth_views.LoginView.as_view(
      template_name='usuario/'
    ), name='login'),
   #path('users/', usuarios, 'usuarios.html')
] 
""" + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """
