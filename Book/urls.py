from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),  # Ruta principal que carga la vista index
    path('palindromo/<str:palabra>/', views.verificar_palindromo, name='verificar_palindromo'),
    path('palindromo/', views.verificar_palindromo_param, name='verificar_palindromo_param'),  # URL para procesar el palíndromo
    path('listbook/', views.listar_libros, name='listar_libros'),
    path('listbook/high/', views.listar_libros_valoracion, name='listar_libros_valoracion'),
    path('inputbook/', views.inputbook, name='inputbook'),
    path('success/', views.success, name='success'),
    path('registro/', views.registro, name='registro'),
    path('listar_libros/', views.listar_librosbd, name='listar_libros1'),
    #path('listbook/valoracion-alta/', views.libros_valoracion_alta, name='libros_valoracion_alta'),
    #path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    #path('cargar-libros-csv/', views.cargar_libros_csv, name='cargar_libros_csv'),

]
