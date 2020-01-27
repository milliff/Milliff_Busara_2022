# Generated by Django 2.2.4 on 2020-01-26 14:48

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_survey', '0031_auto_20200126_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='belief_behav',
            field=otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walikuwa na tabia iliyo wafanya walengwe, au walikuwa na kitu ambacho kiliwafanya  walengwa'),
        ),
        migrations.AlterField(
            model_name='player',
            name='belief_ident',
            field=otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walilenga kwa sababu ya kabila, jinsia au ukoo au kitu kingine kinacho watambulisha'),
        ),
        migrations.AlterField(
            model_name='player',
            name='belief_rand',
            field=otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani kilichotokea kwao ni bahati mbaya tu'),
        ),
        migrations.AlterField(
            model_name='player',
            name='belief_situ',
            field=otree.db.models.StringField(choices=[['Does not describe my belief', 'Haielezi maoni yangu hata kidogo'], ['Slightly describes my belief', 'Slightly describes my belief'], ['Moderately describes my belief', 'Inaeleza maoni yangu kiasi'], ['Mostly describes my belief', 'Inaelezea maoni yangu kwa kiwango kubwa'], ['Completely describes my belief', 'Inaelezea maoni yangu kabisa']], max_length=10000, null=True, verbose_name='Nadhani walikuwa mahali  pasipofaa kwa wakati usiofaa'),
        ),
    ]
