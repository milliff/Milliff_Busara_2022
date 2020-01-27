# Generated by Django 2.2.4 on 2020-01-26 14:45

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_survey', '0022_auto_20200126_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='belief_indiv',
            field=otree.db.models.StringField(choices=[['Does not describe my belief', 'Does not describe my belief'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Moderately describes my belief'], ['Mostly describes my belief', 'Mostly describes my belief'], ['Completely describes my belief', 'Completely describes my belief']], max_length=10000, null=True, verbose_name='Nadhani walilenga kama mtu binafsi na watu ambao walijua ni nani wanalenga'),
        ),
    ]
