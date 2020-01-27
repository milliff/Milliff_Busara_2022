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
Pre Survey; Busara Omnibus module
Version: 24 Jan 2020
"""


class Constants(BaseConstants):
    name_in_url = 'pre_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    exp_murder = models.BooleanField(label="Mauaji, au kuchomwa",
                          widget=widgets.CheckboxInput, blank=True,
                                     choices=[[False, 'False'],
                                              [True, 'True']])
    exp_assault = models.BooleanField(label="Kushambuliwa",
                          widget=widgets.CheckboxInput, blank=True,
                                     choices=[[False, 'False'],
                                              [True, 'True']])
    exp_mugging = models.BooleanField(label="Kuibiwa kwa nguvu",
                          widget=widgets.CheckboxInput, blank=True,
                                     choices=[[False, 'False'],
                                              [True, 'True']])
    exp_dvgbf = models.BooleanField(label="Vurugu za kinyumbani au vita vya mke na mume",
                        widget=widgets.CheckboxInput, blank=True,
                                     choices=[[False, 'False'],
                                              [True, 'True']])
    exp_riot = models.BooleanField(label="Vurugu za polisi",
                          widget=widgets.CheckboxInput, blank=True,
                                     choices=[[False, 'False'],
                                              [True, 'True']])
    exp_arson = models.BooleanField(label="Kuchomewa vitu/mali",
                          widget=widgets.CheckboxInput, blank=True,
                                     choices=[[False, 'False'],
                                              [True, 'True']])
    exp_witchcraft = models.BooleanField(label="Uchawi",
                          widget=widgets.CheckboxInput, blank=True,
                                     choices=[[False, 'False'],
                                              [True, 'True']])
    exp_other = models.BooleanField(label="Nyingine/Hapana",
                          widget=widgets.CheckboxInput, blank=True,
                                     choices=[[False, 'False'],
                                              [True, 'True']])
    # prior_exposure = tool_models.MultipleChoiceModelField(label="Please select all that apply to you:", # Come back to this and add choice randomizer https://otree.readthedocs.io/en/latest/forms.html#dynamic-form-field-validation
    #                                                           min_choices=0, max_choices=8, blank=True
    #                                                       # choices=[["murder", "Murder, homicide, or lynching"],
    #                                                       #          ["assault", "Assault or attack"],
    #                                                       #          ["mugging", "Mugging"],
    #                                                       #          ["dv_gbf", "Domestic violence or gender-based violence"],
    #                                                       #          ["riot_police", "Riot violence or police violence"],
    #                                                       #          ["arson", "Arson"],
    #                                                       #          ["witchcraft", "Witchcraft"],
    #                                                       #          ["other", "Other"]]
    #                                                                )
    victim = models.StringField(label="Kwa kila tukio liliofanyika hivi karibuni, muathirika alikuwa ni nani?",
                                widget=widgets.RadioSelect,
                                choices=[["self", "Mimi Mwenyewe"],
                                         ["parent_child_spouse", "Wazazi wangu, mtoto wangu ama mpenzi wangu"],
                                         ["other_family", "Mtu mwingine kwenye familia"],
                                         ["neighbor_friend", "Rafiki wa karibu ama jirani"],
                                         ["someone_else", "Mtu mwingine ninaye mjua"]])
    belief_indiv = models.StringField(label="Nadhani walilenga kama mtu binafsi na watu ambao walijua ni nani wanalenga",
                                      widget=widgets.RadioSelect, choices=[["Does not describe my belief","Haielezi maoni yangu hata kidogo"],
                                                                            ["Slightly describes my belief", "Slightly describes my belief"],
                                                                            ["Moderately describes my belief", "Inaeleza maoni yangu kiasi"],
                                                                            ["Mostly describes my belief", "Inaelezea maoni yangu kwa kiwango kubwa"],
                                                                            ["Completely describes my belief", "Inaelezea maoni yangu kabisa"]])
    belief_ident = models.StringField(label="Nadhani walilenga kwa sababu ya kabila, jinsia au ukoo au kitu kingine kinacho watambulisha",
                                      widget=widgets.RadioSelect, choices=[["Does not describe my belief","Haielezi maoni yangu hata kidogo"],
                                                                            ["Slightly describes my belief", "Slightly describes my belief"],
                                                                            ["Moderately describes my belief", "Inaeleza maoni yangu kiasi"],
                                                                            ["Mostly describes my belief", "Inaelezea maoni yangu kwa kiwango kubwa"],
                                                                            ["Completely describes my belief", "Inaelezea maoni yangu kabisa"]])
    belief_situ  = models.StringField(label="Nadhani walikuwa mahali  pasipofaa kwa wakati usiofaa",
                                      widget=widgets.RadioSelect, choices=[["Does not describe my belief","Haielezi maoni yangu hata kidogo"],
                                                                            ["Slightly describes my belief", "Slightly describes my belief"],
                                                                            ["Moderately describes my belief", "Inaeleza maoni yangu kiasi"],
                                                                            ["Mostly describes my belief", "Inaelezea maoni yangu kwa kiwango kubwa"],
                                                                            ["Completely describes my belief", "Inaelezea maoni yangu kabisa"]])
    belief_behav = models.StringField(label="Nadhani walikuwa na tabia iliyo wafanya walengwe, au walikuwa na kitu ambacho kiliwafanya  walengwa",
                                      widget=widgets.RadioSelect, choices=[["Does not describe my belief","Haielezi maoni yangu hata kidogo"],
                                                                            ["Slightly describes my belief", "Slightly describes my belief"],
                                                                            ["Moderately describes my belief", "Inaeleza maoni yangu kiasi"],
                                                                            ["Mostly describes my belief", "Inaelezea maoni yangu kwa kiwango kubwa"],
                                                                            ["Completely describes my belief", "Inaelezea maoni yangu kabisa"]])
    belief_rand  = models.StringField(label="Nadhani kilichotokea kwao ni bahati mbaya tu",
                                      widget=widgets.RadioSelect, choices=[["Does not describe my belief","Haielezi maoni yangu hata kidogo"],
                                                                            ["Slightly describes my belief", "Slightly describes my belief"],
                                                                            ["Moderately describes my belief", "Inaeleza maoni yangu kiasi"],
                                                                            ["Mostly describes my belief", "Inaelezea maoni yangu kwa kiwango kubwa"],
                                                                            ["Completely describes my belief", "Inaelezea maoni yangu kabisa"]])


    def get_booleans(self):
        exp = [self.exp_murder, self.exp_assault, self.exp_mugging,
               self.exp_dvgbf, self.exp_riot, self.exp_arson,
               self.exp_witchcraft, self.exp_other]
        exp_ct = sum(bool(x) for x in exp)
        return exp_ct
