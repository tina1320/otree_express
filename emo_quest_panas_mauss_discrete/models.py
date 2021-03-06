from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Kristian'

doc = """
Panas + Mauss
"""


class Constants(BaseConstants):
    name_in_url = 'PANAS_MAUSS'
    players_per_group = None
    num_rounds = 1
    panasmauss_list = [
         'Active',
         'Excited',
         'Angry',
         'Interested',
         'Sad',
         'Gratitude',
         'Upset',
         'Proud',
         'Happy',
         'Hostile',
         'Anxious',
         'Strong',
         'Loving',
         'Distressed',
         'Guilty',
         'Calm',
         'Nervous',
         'Scared',
         'Determined',
         'Annoyed',
         'Inspired',
         'Positive (feel good)',
         'Alert',
         'Energetic',
         'Negative (feel bad)',
         'Jittery',
         'Ashamed',
         'Amused',
         'Attentive',
         'Irritable',
         'Enthusiastic',
         'Afraid'
    ]

        # list sizes
    list_size = len(panasmauss_list)
    num_emo_pg1 = int(round(list_size / 2, 0))
    num_emo_pg2 = list_size - num_emo_pg1


class Subsession(BaseSubsession):

    def before_session_starts(self):
        panasmauss_list = random.sample(Constants.panasmauss_list, len(Constants.panasmauss_list))
        self.session.vars['panasmauss_list_1'] = panasmauss_list[:Constants.num_emo_pg1]
        self.session.vars['panasmauss_list_2'] = panasmauss_list[Constants.num_emo_pg1:]

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_EmoQuestPage1 = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_EmoQuestPage2 = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    # list = random.sample(Constants.panasmauss_list, len(Constants.panasmauss_list))


for var in Constants.panasmauss_list:
    Player.add_to_class(
        'panasmauss_{}'.format(var),
        models.IntegerField(
            initial=None,
            choices=[
                [1, '1'],
                [2, '2'],
                [3, '3'],
                [4, '4'],
                [5, '5'],
                [6, '6'],
                [7, '7']
                ],
            verbose_name=var,
            widget=widgets.RadioSelectHorizontal()
        )
        )

# [1, '1 (Not at all)'],
# [2, '2'],
# [3, '3'],
# [4, '4 (Moderately)'],
# [5, '5'],
# [6, '6'],
# [7, '7 (Extremely)']
#

# for emotion in range(10):
#     Group.add_to_class(
#         'cash_{}'.format(amount),
#         models.BooleanField(
#             widget=widgets.RadioSelectHorizontal(),
#             choices=[[True, ''], [False, '']],
#             verbose_name='{}'.format(c(amount))
#         )
#     )

###################
# DRAFT

# for i in range(len(Constants.emotion_list)):
#     temp = '_'.join(Constants.emotion_list[i])
#     print(temp)
#     Player.add_to_class(
#         '{}'.format(temp),
#         models.DecimalField(max_digits=5, decimal_places=2, min=0, max=10)
#     )
