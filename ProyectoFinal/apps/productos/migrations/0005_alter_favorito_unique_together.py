# Generated by Django 5.0.6 on 2024-06-14 03:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_rename_usuario_favorito_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorito',
            unique_together={('user', 'producto')},
        ),
    ]
