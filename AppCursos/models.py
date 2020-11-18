from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.urls import reverse

# Create your models here.

class categorias(models.Model):
    nombre= models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)   
    updated = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return self.nombre

class Cursos(models.Model):
    titulo = models.CharField(max_length=20)
    overview = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to='Cursos/curso')
    fecha = models.DateField(auto_now_add=True)

    autor = models.ForeignKey(User, on_delete = models.CASCADE)    
    categorias = models.ManyToManyField(categorias)

    contenido= HTMLField()

    created = models.DateTimeField(auto_now_add=True)                   
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("cursos_detallados", kwargs={"curso_id": self.id})

    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-fecha')

class Comentarios(models.Model):

    usuario = models.ForeignKey(User, on_delete = models.CASCADE)   
    fecha = models.DateTimeField(auto_now_add=True)
    content = models.TextField()                                 
    curso = models.ForeignKey('Cursos', related_name='comments', on_delete = models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)                   
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username