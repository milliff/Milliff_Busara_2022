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
Manipulation checks, post treatment
"""


class Constants(BaseConstants):
    name_in_url = 'manipulation_check'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sense_control = models.StringField(label="Ulihisi una uwezo kiasi gani kudhibiti alama ulizopokea kwenye mchezo uliocheza sasa hivi?",
                                       widget=widgets.RadioSelect,
                                       choices=[["None","Hakuna hata kidogo"],
                                                ["Little", "Kidogo"],
                                                ["Moderate", "Wastani"],
                                                ["A Lot", "Kiwango kiKubwa"],
                                                ["Complete control", "Kiwango kikubwa sana"]])
    stai_calm = models.StringField(label = "Nahisi utulivu",
                                   widget=widgets.RadioSelect,
                                   choices=[["None","Hakuna hata kidogo"],
                                            ["Little", "Kidogo"],
                                            ["Moderate", "Wastani"],
                                            ["Very much", "Kiwango kikubwa sana"]])
    stai_tense = models.StringField(label = "Niko na hofu",
                                   widget=widgets.RadioSelect,
                                   choices=[["None","Hakuna hata kidogo"],
                                            ["Little", "Kidogo"],
                                            ["Moderate", "Wastani"],
                                            ["Very much", "Kiwango kikubwa sana"]])
    stai_upset = models.StringField(label = "Nihisi kukasiraka",
                                   widget=widgets.RadioSelect,
                                   choices=[["None","Hakuna hata kidogo"],
                                            ["Little", "Kidogo"],
                                            ["Moderate", "Wastani"],
                                            ["Very much", "Kiwango kikubwa sana"]])
    stai_relaxed = models.StringField(label = "Niko mtulivu",
                                   widget=widgets.RadioSelect,
                                   choices=[["None","Hakuna hata kidogo"],
                                            ["Little", "Kidogo"],
                                            ["Moderate", "Wastani"],
                                            ["Very much", "Kiwango kikubwa sana"]])
    stai_content = models.StringField(label = "Nahisi kuridhika",
                                   widget=widgets.RadioSelect,
                                   choices=[["None","Hakuna hata kidogo"],
                                            ["Little", "Kidogo"],
                                            ["Moderate", "Wastani"],
                                            ["Very much", "Kiwango kikubwa sana"]])
    stai_worried = models.StringField(label = "Nina wasiwasi",
                                   widget=widgets.RadioSelect,
                                   choices=[["None","Hakuna hata kidogo"],
                                            ["Little", "Kidogo"],
                                            ["Moderate", "Wastani"],
                                            ["Very much", "Kiwango kikubwa sana"]])
