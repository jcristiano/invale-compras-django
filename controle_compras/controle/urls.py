from django.urls import path
from controle import views

urlpatterns = [
    path('categoria/adicionar', views.categoria_adicionar, name="controle.categoria_adicionar"),
]