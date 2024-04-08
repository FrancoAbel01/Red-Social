# Generated by Django 4.1.3 on 2023-02-14 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_alter_post_content_alter_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('contenido', models.CharField(blank=True, max_length=30, null=True)),
                ('like', models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL)),
                ('postCom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postsCom', to='app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-hora'],
            },
        ),
    ]