from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class Instruction(Page):
    pass
    # def is_displayed(self):
    #     return self.round_number == 1

class Instruction_2(Page):
    pass


class Task1(Page):
    form_model = models.Player
    form_fields = ['catches', 'score']

    def vars_for_template(self):
        return {
            'prize': -5
        }

    def before_next_page(self):
        self.player.set_payoff()

class Results(Page):
    pass

class task_wait(WaitPage):
    pass



page_sequence = [
    Instruction,
    Instruction_2,
    Task1,
    task_wait,
    Results,
]
