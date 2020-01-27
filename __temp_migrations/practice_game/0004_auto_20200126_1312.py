# Generated by Django 2.2.4 on 2020-01-26 10:12

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_game', '0003_auto_20200126_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='misses',
        ),
        migrations.AddField(
            model_name='player',
            name='hits',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
