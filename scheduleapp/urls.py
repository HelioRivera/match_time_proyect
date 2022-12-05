from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recibir_disponibilidad_horaria/<str:dia>/<str:jornada>/<str:hora>', views.recibir_disponibilidad_horaria),
]
