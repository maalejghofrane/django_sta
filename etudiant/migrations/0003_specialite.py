# Generated by Django 3.2 on 2021-04-27 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0002_auto_20210420_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=70)),
                ('niveau', models.EmailField(max_length=100)),
            ],
        ),
    ]