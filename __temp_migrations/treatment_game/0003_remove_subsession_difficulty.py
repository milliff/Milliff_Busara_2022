# Generated by Django 2.2.4 on 2020-01-26 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treatment_game', '0002_subsession_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subsession',
            name='difficulty',
        ),
    ]