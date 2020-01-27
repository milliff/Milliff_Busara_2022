from ._builtin import Page, WaitPage
import random


class exp_page(Page):
    form_model = "player"
    form_fields = ["exp_murder", "exp_assault", "exp_mugging",
                   "exp_dvgbf", "exp_riot", "exp_arson", "exp_witchcraft",
                   "exp_other"]

    def vars_for_template(self):
        booleans = self.player.get_booleans();
        print("booleans: ", booleans)
        return dict(booleans=booleans)
        # exp = [self.player.exp_murder, self.player.exp_assault, self.player.exp_mugging,
        #           self.player.exp_dvgbf, self.player.exp_riot, self.player.exp_arson,
        #           self.player.exp_witchcraft, self.player.exp_other]
        # exp_ct = sum(bool(x) for x in exp)
        # return exp_ct


class vic_page(Page):
    form_model = "player"
    form_fields = ["victim"]


    def is_displayed(self):
        exp_ct = self.player.get_booleans()
        return exp_ct != 0


class exp_wait_page(WaitPage):
    pass


class belief_page(Page):
    form_model = "player"
    form_fields = ["belief_indiv", "belief_ident",
                   "belief_situ", "belief_behav",
                   "belief_rand"]

    def vars_for_template(self):
        exp_ct = self.player.get_booleans()
        vic_self = self.player.victim
        return dict(exp_ct=exp_ct,
                    vic_self = vic_self)

class intro_page(Page):
    pass

class intro_2(Page):
    pass

page_sequence = [intro_page,
                 intro_2,
                 exp_page,
                 vic_page,
                 exp_wait_page,
                 belief_page]
