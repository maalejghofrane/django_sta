# Generated by Django 3.2 on 2021-04-27 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matiere', '0003_matiere_module'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matiere',
            old_name='Module',
            new_name='module',
        ),
    ]
