# Generated by Django 3.2 on 2021-04-27 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
        ('matiere', '0004_rename_module_matiere_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matiere',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module.module'),
        ),
    ]
