# Generated by Django 3.2 on 2021-04-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='niveau',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tel',
            field=models.IntegerField(null=True),
        ),
    ]
