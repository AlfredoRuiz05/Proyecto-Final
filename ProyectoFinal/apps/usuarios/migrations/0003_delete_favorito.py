# Generated by Django 5.0.6 on 2024-06-13 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_email_alter_usuario_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorito',
        ),
    ]