from django.urls import path
from AppCursos import views

urlpatterns = [
    path('', views.cursos, name='cursos'),
    path('arts/', views.arts, name='arts'),
    path('languages/', views.languages, name='languages'),
    path('<int:curso_id>/', views.cursos_detallados, name='cursos_detallados'), 
]