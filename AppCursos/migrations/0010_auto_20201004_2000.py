# Generated by Django 3.0.5 on 2020-10-05 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCursos', '0009_auto_20201004_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentarios',
            old_name='user',
            new_name='usuario',
        ),
        migrations.AddField(
            model_name='comentarios',
            name='imagen_usuario',
            field=models.ImageField(default='default', upload_to='Cursos/usuario'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
