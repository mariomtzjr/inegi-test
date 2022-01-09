from django.urls import path

from api import views

urlpatterns = [
    path('entidades/listar/<str:ef>/<str:mun>/<str:establecimiento>/', views.ListEntities.as_view(), name="entity-list"),
]