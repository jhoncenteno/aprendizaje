# Generated by Django 3.0.5 on 2020-10-05 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCursos', '0011_remove_comentarios_imagen_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentarios',
            old_name='course',
            new_name='curso',
        ),
    ]
