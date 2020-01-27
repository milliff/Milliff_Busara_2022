from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class ego(Page):
    form_model = "player"
    form_fields = ["outcome1_ego"]
    timeout_seconds = 11

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout = True

class alter(Page):
    form_model = "player"
    form_fields = ["outcome1_alter"]
    timeout_seconds = 11

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout = True

class control(Page):
    form_model = "player"
    form_fields = ["outcome1_control"]

class belief(Page):
    form_model = "player"
    form_fields = ["outcome1_indiv", "outcome1_ident",
                   "outcome1_situ", "outcome1_behav",
                   "outcome1_rand"]


page_sequence = [Instructions, ego, alter, control, belief]
