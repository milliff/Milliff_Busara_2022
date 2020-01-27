from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class control_sense(Page):
    form_model = "player"
    form_fields = ["sense_control"]

class stai(Page):
    form_model = "player"
    form_fields = ["stai_calm", "stai_tense", "stai_upset",
                   "stai_relaxed", "stai_content", "stai_worried"]


page_sequence = [control_sense, stai]
