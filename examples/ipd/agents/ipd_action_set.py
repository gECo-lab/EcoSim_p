# -*- coding: utf-8 -*-
""" Basic Strategy Class implementation """

import random
import copy


class Game:
    """ Class Representing a Game """

    def __init__(self, my_name=None, my_play=None, my_payoff=None,
                 other_name=None, other_play=None, other_payoff=None):
        self.my_name = my_name
        self.my_play = my_play
        self.my_payoff = my_payoff
        self.other_name = other_name
        self.other_play = other_play
        self.other_payoff = other_payoff


class Strategy:
    """ Implementation of the strategy class """
    def __init__(self):
        self.strategy_name = "general"
        self.strategy = "C"
        self.game = Game("", "C", 3, "", "C", 3)
        self.last_game = Game("", "C", 3, "", "C", 3)

    def select_game(self):
        return self.strategy

    def update_game(self, aGame):
        """ Get a game """
        self.last_game = copy.copy(self.game)
        self.game = aGame


class AlwaysCooperate(Strategy):
    """ Always Cooperate Strategy """
    def __init__(self):
        super().__init__()
        self.strategy_name = "cooperate"
        self.strategy = "C"


class AlwaysDefect(Strategy):
    def __init__(self):
        super().__init__()
        self.strategy_name = "defect"
        self.strategy = "D"


class RandomPlay(Strategy):
    def __init__(self):
        super().__init__()
        self.strategy_name = "random"
        self.strategy = ["D", "C"]

    def select_game(self):
        """ Random Strategy """
        return random.choice(self.strategy)


class SimpleTitForTat(Strategy):
    def __init__(self):
        super().__init__()
        self.strategy_name = "simpleTitForTat"
        self.other_last_strategy = "C"
        self.selected_strategy = "C"

    def select_game(self):
        """ Simple Tit for tat strategy """
        if self.last_game.other_play == "C":
            self.selected_strategy = "C"
        else:
            self.selected_strategy = "D"

        return self.selected_strategy
