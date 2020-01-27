# Generated by Django 2.2.4 on 2020-01-26 14:39

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_survey', '0017_auto_20200126_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='victim',
            field=otree.db.models.StringField(choices=[['self', 'Mimi Mwenyewe'], ['parent_child_spouse', 'Wazazi wangu, mtoto wangu ama mpenzi wangu'], ['other_family', 'Another family member'], ['neighbor_friend', 'A neighbor or close friend'], ['someone_else', 'Someone else I know']], max_length=10000, null=True, verbose_name='In the most recent incident, who was the victim?'),
        ),
    ]
