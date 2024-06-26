# Generated by Django 4.0.6 on 2023-08-06 20:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0014_profile_city_profile_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='likes',
            field=models.ManyToManyField(related_name='likesComentario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='contenido',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='imag.png', upload_to=''),
        ),
    ]
