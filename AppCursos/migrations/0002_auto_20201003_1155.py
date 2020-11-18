# Generated by Django 3.0.5 on 2020-10-03 15:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='overview',
            field=models.TextField(default='test', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cursos',
            name='contenido',
            field=tinymce.models.HTMLField(),
        ),
    ]
