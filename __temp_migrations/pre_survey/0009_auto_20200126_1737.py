# Generated by Django 2.2.4 on 2020-01-26 14:37

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_survey', '0008_auto_20200126_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='exp_murder',
            field=otree.db.models.BooleanField(blank=True, choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='Mauaji, au kuchomwa'),
        ),
    ]