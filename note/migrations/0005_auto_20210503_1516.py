# Generated by Django 3.2 on 2021-05-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_note_moy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='moy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_ds',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_exam',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_tp',
            field=models.FloatField(),
        ),
    ]
