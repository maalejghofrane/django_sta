# Generated by Django 3.2 on 2021-04-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matiere', '0007_alter_matiere_ds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matiere',
            name='ds',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='exam',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='tp',
            field=models.IntegerField(),
        ),
    ]