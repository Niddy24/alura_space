# Generated by Django 5.0.6 on 2024-07-05 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='legemda',
            new_name='legenda',
        ),
    ]
