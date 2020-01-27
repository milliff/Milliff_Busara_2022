from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions_1(Page):
    pass

class Audio_Page(Page):
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass



page_sequence = [Instructions_1, Audio_Page]
