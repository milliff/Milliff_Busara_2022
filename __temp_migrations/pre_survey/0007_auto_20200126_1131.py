# Generated by Django 2.2.4 on 2020-01-26 08:31

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_survey', '0006_auto_20200126_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='belief_behav',
            field=otree.db.models.StringField(choices=[[0, 'Does not describe my belief'], [1, 'Slightly describes my belief'], [2, 'Moderately describes my belief'], [3, 'Mostly describes my belief'], [4, 'Completely describes my belief']], max_length=10000, null=True, verbose_name='I think the perpetrator chose a target based on something they were doing or something they had that made them a target'),
        ),
        migrations.AlterField(
            model_name='player',
            name='belief_ident',
            field=otree.db.models.StringField(choices=[[0, 'Does not describe my belief'], [1, 'Slightly describes my belief'], [2, 'Moderately describes my belief'], [3, 'Mostly describes my belief'], [4, 'Completely describes my belief']], max_length=10000, null=True, verbose_name='I think the perpetrator chose their target based on tribe, clan, gender, or some other part of identity'),
        ),
        migrations.AlterField(
            model_name='player',
            name='belief_indiv',
            field=otree.db.models.StringField(choices=[[0, 'Does not describe my belief'], [1, 'Slightly describes my belief'], [2, 'Moderately describes my belief'], [3, 'Mostly describes my belief'], [4, 'Completely describes my belief']], max_length=10000, null=True, verbose_name='I think the perpetrator was looking for a specific person'),
        ),
        migrations.AlterField(
            model_name='player',
            name='belief_rand',
            field=otree.db.models.StringField(choices=[[0, 'Does not describe my belief'], [1, 'Slightly describes my belief'], [2, 'Moderately describes my belief'], [3, 'Mostly describes my belief'], [4, 'Completely describes my belief']], max_length=10000, null=True, verbose_name='I think what happened was just random'),
        ),
        migrations.AlterField(
            model_name='player',
            name='belief_situ',
            field=otree.db.models.StringField(choices=[[0, 'Does not describe my belief'], [1, 'Slightly describes my belief'], [2, 'Moderately describes my belief'], [3, 'Mostly describes my belief'], [4, 'Completely describes my belief']], max_length=10000, null=True, verbose_name='I think it was just a matter of being in the wrong place at the wrong time'),
        ),
    ]