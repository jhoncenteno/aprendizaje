from django.shortcuts import render, get_object_or_404, redirect
from AppCursos.models import categorias, Cursos
from AppCursos.forms import FormularioComentarios
# Create your views here.

def cursos(request):

    cursos = Cursos.objects.all()

    return render (request, '2curso.html', {'cursos' : cursos})


def arts(request):

    lista_arts = Cursos.objects.filter(categorias__nombre="Arts")

    return render (request, '2.1arts.html', {'lista_arts' : lista_arts})

def languages(request):

    lista_languages = Cursos.objects.filter(categorias__nombre="Languages")

    return render (request, '2.2languages.html', {'lista_languages' : lista_languages})


def cursos_detallados(request, curso_id):
    
    curso= get_object_or_404(Cursos, id= curso_id)
    formulario = FormularioComentarios(request.POST or None) 

    if request.method == "POST":
        if formulario.is_valid():
            formulario.instance.usuario = request.user       
            formulario.instance.curso = curso
            formulario.save()
            return redirect('cursos_detallados', curso_id = curso_id)


    return render(request, '3curso_detallado.html', { "curso" : curso, "formulario" : formulario })

