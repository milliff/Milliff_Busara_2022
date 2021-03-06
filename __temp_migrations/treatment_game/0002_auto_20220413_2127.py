# Generated by Django 2.2.12 on 2022-04-14 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treatment_game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment_game.Subsession'),
        ),
        migrations.AlterField(
            model_name='player',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='treatment_game.Group'),
        ),
        migrations.AlterField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment_game.Subsession'),
        ),
    ]
