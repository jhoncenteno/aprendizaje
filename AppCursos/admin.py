from django.contrib import admin
from AppCursos.models import categorias, Cursos, Comentarios

# Register your model here

class categoriasadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')   

class cursosadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  

class comentariosadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  


admin.site.register(categorias, categoriasadmin)
admin.site.register(Cursos, cursosadmin)
admin.site.register(Comentarios, comentariosadmin)