# Generated by Django 4.1.3 on 2023-02-15 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_remove_comentario_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='postCom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postCom', to='app.post'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to=settings.AUTH_USER_MODEL),
        ),
    ]
