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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_survey_group', to='otree.Session')),
            ],
            options={
                'db_table': 'pre_survey_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pre_survey_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'pre_survey_subsession',
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
                ('exp_murder', otree.db.models.BooleanField(blank=True, choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='Mauaji, au kuchomwa')),
                ('exp_assault', otree.db.models.BooleanField(blank=True, choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='Kushambuliwa')),
                ('exp_mugging', otree.db.models.BooleanField(blank=True, choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='Kuibiwa kwa nguvu')),
                ('exp_dvgbf', otree.db.models.BooleanField(blank=True, choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='Vurugu za kinyumbani au vita vya mke na mume')),
                ('exp_riot', otree.db.models.BooleanField(blank=True, choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='Vurugu za polisi')),
                ('exp_arson', otree.db.models.BooleanField(blank=True, choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='Kuchomewa vitu/mali')),
                ('exp_witchcraft', otree.db.models.BooleanField(blank=True, choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='Uchawi')),
                ('exp_other', otree.db.models.BooleanField(blank=True, choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='Nyingine/Hapana')),
                ('victim', otree.db.models.StringField(choices=[['self', 'Mimi Mwenyewe'], ['parent_child_spouse', 'Wazazi wangu, mtoto wangu ama mpenzi wangu'], ['other_family', 'Mtu mwingine kwenye familia'], ['neighbor_friend', 'Rafiki wa karibu ama jirani'], ['someone_else', 'Mtu mwingine ninaye mjua']], max_length=10000, null=True, verbose_name='Kwa kila tukio liliofanyika hivi karibuni, muathirika alikuwa ni nani?')),
                ('belief_indiv', otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walilenga kama mtu binafsi na watu ambao walijua ni nani wanalenga')),
                ('belief_ident', otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walilenga kwa sababu ya kabila, jinsia au ukoo au kitu kingine kinacho watambulisha')),
                ('belief_situ', otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walikuwa mahali  pasipofaa kwa wakati usiofaa')),
                ('belief_behav', otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walikuwa na tabia iliyo wafanya walengwe, au walikuwa na kitu ambacho kiliwafanya  walengwa')),
                ('belief_rand', otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani kilichotokea kwao ni bahati mbaya tu')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pre_survey.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_survey_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_survey_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pre_survey.Subsession')),
            ],
            options={
                'db_table': 'pre_survey_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pre_survey.Subsession'),
        ),
    ]
