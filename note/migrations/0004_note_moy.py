# Generated by Django 3.2 on 2021-04-27 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_note_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='moy',
            field=models.IntegerField(null=True),
        ),
    ]
