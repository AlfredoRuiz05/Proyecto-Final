# Generated by Django 5.0.6 on 2024-06-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuario_es_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='es_admin',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]