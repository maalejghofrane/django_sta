# Generated by Django 3.2 on 2021-04-27 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0004_user_specialite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialite',
            name='niveau',
            field=models.CharField(max_length=100),
        ),
    ]
