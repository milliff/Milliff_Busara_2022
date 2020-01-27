from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Aidan Milliff'

doc = """
Outcome Survey 2
"""


class Constants(BaseConstants):
    name_in_url = 'outcome_2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    outcome2_ego = models.StringField(label="Mtu huyo anafaa kufanya nini??",
                                     widget=widgets.RadioSelect,
                                     choices=[["fight", "Apigane kujikinga"],
                                              ['flee', "Atoroke"],
                                              ['hide', "Ajifiche gizani"],
                                              ["donothing", "Asifanye chochote"],
                                              ["learnmore", "Nahitaji kujua zaidi ili kufanya uamuzi"]])
    outcome2_alter = models.StringField(label="Unafikiri watu wengine wangechagua mtu huyu kufanya nini?",
                                     widget=widgets.RadioSelect,
                                     choices=[["fight", "Apigane kujikinga"],
                                              ['flee', "Atoroke"],
                                              ['hide', "Ajifiche gizani"],
                                              ["donothing", "Asifanye chochote"],
                                              ["learnmore", "Nahitaji kujua zaidi ili kufanya uamuzi"]])
    outcome2_control = models.StringField(label="Unahisi mtu huyu alikuwa na udhibiti kiasi gani katika hali hii?",
                                       widget=widgets.RadioSelect,
                                       choices=[["None","Hakuna hata kidogo"],
                                                ["Little", "Kidogo"],
                                                ["Moderate", "Wastani"],
                                                ["A Lot", "Kiwango kiKubwa"],
                                                ["Complete control", "Kiwango kikubwa sana"]])
    outcome2_indiv = models.StringField(label="Nadhani walilenga kama mtu binafsi na watu ambao walijua ni nani wanalenga",
                                      widget=widgets.RadioSelect, choices=[["Does not describe my belief","Haielezi maoni yangu hata kidogo"],
                                                                            ["Slightly describes my belief", "Slightly describes my belief"],
                                                                            ["Moderately describes my belief", "Inaeleza maoni yangu kiasi"],
                                                                            ["Mostly describes my belief", "Inaelezea maoni yangu kwa kiwango kubwa"],
                                                                            ["Completely describes my belief", "Inaelezea maoni yangu kabisa"]])

    outcome2_ident = models.StringField(label="Nadhani walilenga kwa sababu ya kabila, jinsia au ukoo au kitu kingine kinacho watambulisha",
                                      widget=widgets.RadioSelect, choices=[["Does not describe my belief","Haielezi maoni yangu hata kidogo"],
                                                                            ["Slightly describes my belief", "Slightly describes my belief"],
                                                                            ["Moderately describes my belief", "Inaeleza maoni yangu kiasi"],
                                                                            ["Mostly describes my belief", "Inaelezea maoni yangu kwa kiwango kubwa"],
                                                                            ["Completely describes my belief", "Inaelezea maoni yangu kabisa"]])

    outcome2_situ = models.StringField(label="Nadhani walikuwa mahali  pasipofaa kwa wakati usiofaa",
                                      widget=widgets.RadioSelect, choices=[["Does not describe my belief","Haielezi maoni yangu hata kidogo"],
                                                                            ["Slightly describes my belief", "Slightly describes my belief"],
                                                                            ["Moderately describes my belief", "Inaeleza maoni yangu kiasi"],
                                                                            ["Mostly describes my belief", "Inaelezea maoni yangu kwa kiwango kubwa"],
                                                                            ["Completely describes my belief", "Inaelezea maoni yangu kabisa"]])

    outcome2_behav = models.StringField(label="Nadhani walikuwa na tabia iliyo wafanya walengwe, au walikuwa na kitu ambacho kiliwafanya  walengwa",
                                      widget=widgets.RadioSelect, choices=[["Does not describe my belief","Haielezi maoni yangu hata kidogo"],
                                                                            ["Slightly describes my belief", "Slightly describes my belief"],
                                                                            ["Moderately describes my belief", "Inaeleza maoni yangu kiasi"],
                                                                            ["Mostly describes my belief", "Inaelezea maoni yangu kwa kiwango kubwa"],
                                                                            ["Completely describes my belief", "Inaelezea maoni yangu kabisa"]])

    outcome2_rand = models.StringField(label="Nadhani kilichotokea kwao ni bahati mbaya tu",
                                      widget=widgets.RadioSelect, choices=[["Does not describe my belief","Haielezi maoni yangu hata kidogo"],
                                                                            ["Slightly describes my belief", "Slightly describes my belief"],
                                                                            ["Moderately describes my belief", "Inaeleza maoni yangu kiasi"],
                                                                            ["Mostly describes my belief", "Inaelezea maoni yangu kwa kiwango kubwa"],
                                                                            ["Completely describes my belief", "Inaelezea maoni yangu kabisa"]])
    timeout = models.BooleanField()


