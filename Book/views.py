

from django.http import HttpResponse

from .models import Libro
from django.shortcuts import render, redirect
#from .forms import LibroForm

import csv

from .forms import LibroForm

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

# Simulación de libros en una lista de diccionarios
libros = [
    {'titulo': 'Libro A', 'autor': 'Autor A', 'valoracion': 1200},
    {'titulo': 'Libro B', 'autor': 'Autor B', 'valoracion': 1600},
    {'titulo': 'Libro C', 'autor': 'Autor C', 'valoracion': 1800},
]


def listar_libros(request):
    # Filtrar los libros con valoración mayor a 1500
    libros_filtrados = [libro for libro in libros if libro['valoracion'] > 1500]
    
    # Pasar ambas listas al template
    context = {
        'libros': libros,
        'libros_filtrados': libros_filtrados
    }
    
    return render(request, 'listar_libros.html', context)


def listar_librosbd(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros1.html', {'libros': libros})



def listar_libros_valoracion(request):
    # Filtrar los libros con valoración mayor a 1500
    libros_filtrados = [libro for libro in libros if libro['valoracion'] > 1500]
    return render(request, 'listar_libros_valoracion.html', {'libros': libros_filtrados})





""" def inputbook(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            # Aquí puedes manejar los datos del formulario, por ejemplo, guardarlos en la base de datos
            # libro = Libro.objects.create(**form.cleaned_data)
            return redirect('success')  # Redirigir a una página de éxito o a donde desees
    else:
        form = LibroForm()
    
    return render(request, 'inputbook.html', {'form': form}) """



def inputbook(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirigir a una página de éxito o a donde desees
    else:
        form = LibroForm()
    
    return render(request, 'inputbook.html', {'form': form})


def success(request):
    return render(request, 'success.html')

def registro(request):
    return render(request, 'registro.html')


def verificar_palindromo(request, palabra):
    # Limpiar la palabra/frase: eliminar espacios y convertir a minúsculas
    palabra_limpia = ''.join(e for e in palabra if e.isalnum()).lower()

    # Verificar si es un palíndromo
    es_palindromo = palabra_limpia == palabra_limpia[::-1]

    # Pasar los resultados a la plantilla
    return render(request, 'palindromo.html', {
        'palabra': palabra,
        'es_palindromo': es_palindromo
    })

def verificar_palindromo_param(request):
    palabra = request.GET.get('palabra', '')

    # Limpiar la palabra/frase: eliminar espacios y convertir a minúsculas
    palabra_limpia = ''.join(e for e in palabra if e.isalnum()).lower()

    # Verificar si es un palíndromo
    es_palindromo = palabra_limpia == palabra_limpia[::-1]

    # Pasar los resultados a la plantilla
    return render(request, 'palindromo.html', {
        'palabra': palabra,
        'es_palindromo': es_palindromo
    })