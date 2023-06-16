from django.urls import include, path
from rest_framework.routers import DefaultRouter
from projectCar import settings
from .views import CarroViewsSet, home, form, create, view, edit, update, delete
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", home, name="home"),
    path("form/", form, name="form"),
    path("create/", create, name="create"),
    path("view/<int:pk>/", view, name="view"),
    path("edit/<int:pk>/", edit, name="edit"),
    path("update/<int:pk>", update, name="update"),
    path("delete/<int:pk>", delete, name="delete"),
    #path("teste/", teste, name="teste"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
