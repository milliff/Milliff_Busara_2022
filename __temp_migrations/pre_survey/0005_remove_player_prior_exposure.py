# Generated by Django 2.2.4 on 2020-01-24 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pre_survey', '0004_auto_20200124_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='prior_exposure',
        ),
    ]