# Generated by Django 2.2.4 on 2020-01-26 14:38

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_survey', '0014_auto_20200126_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='exp_witchcraft',
            field=otree.db.models.BooleanField(blank=True, choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='Uchawi'),
        ),
    ]
