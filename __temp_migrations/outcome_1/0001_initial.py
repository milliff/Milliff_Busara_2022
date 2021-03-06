# Generated by Django 2.2.12 on 2022-04-14 00:17

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcome_1_group', to='otree.Session')),
            ],
            options={
                'db_table': 'outcome_1_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outcome_1_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'outcome_1_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('outcome1_ego', otree.db.models.StringField(choices=[['fight', 'Ajaribu kujitetea mwenyewe'], ['flee', 'Atokee na aende kwa jirani yake'], ['hide', 'Ajifiche kwenye chumba cha kulala'], ['donothing', 'Asifanye chochote'], ['learnmore', 'Nahitaji kujua zaidi ili kufanya uamuzi']], max_length=10000, null=True, verbose_name='Mwanamke huyo anafaa kufanya nini?')),
                ('outcome1_alter', otree.db.models.StringField(choices=[['fight', 'Ajaribu kujitetea mwenyewe'], ['flee', 'Atokee na aende kwa jirani yake'], ['hide', 'Ajifiche kwenye chumba cha kulala'], ['donothing', 'Asifanye chochote'], ['learnmore', 'Nahitaji kujua zaidi ili kufanya uamuzi']], max_length=10000, null=True, verbose_name='Unafikiri watu wengine wangechagua mwanamke huyo kufanya nini??')),
                ('outcome1_control', otree.db.models.StringField(choices=[['None', 'Hakuna hata kidogo'], ['Little', 'Kidogo'], ['Moderate', 'Wastani'], ['A Lot', 'Kiwango kiKubwa'], ['Complete control', 'Kiwango kikubwa sana']], max_length=10000, null=True, verbose_name='Unahisi mwanamke alikuwa na udhibiti gani katika hali hii?')),
                ('outcome1_indiv', otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walilenga kama mtu binafsi na watu ambao walijua ni nani wanalenga')),
                ('outcome1_ident', otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walilenga kwa sababu ya kabila, jinsia au ukoo au kitu kingine kinacho watambulisha')),
                ('outcome1_situ', otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walikuwa mahali  pasipofaa kwa wakati usiofaa')),
                ('outcome1_behav', otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walikuwa na tabia iliyo wafanya walengwe, au walikuwa na kitu ambacho kiliwafanya  walengwa')),
                ('outcome1_rand', otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani kilichotokea kwao ni bahati mbaya tu')),
                ('timeout', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='outcome_1.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcome_1_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcome_1_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outcome_1.Subsession')),
            ],
            options={
                'db_table': 'outcome_1_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outcome_1.Subsession'),
        ),
    ]
