from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class ego(Page):
    form_model = "player"
    form_fields = ["outcome2_ego"]
    timeout_seconds = 11
    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout = True

class alter(Page):
    form_model = "player"
    form_fields = ["outcome2_alter"]
    timeout_seconds = 11
    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout = True

class control(Page):
    form_model = "player"
    form_fields = ["outcome2_control"]

class belief(Page):
    form_model = "player"
    form_fields = ["outcome2_indiv", "outcome2_ident",
                   "outcome2_situ", "outcome2_behav",
                   "outcome2_rand"]


page_sequence = [Instructions, ego, alter, control, belief]
