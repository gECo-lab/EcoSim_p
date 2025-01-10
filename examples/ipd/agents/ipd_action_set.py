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

    def select_game(self, other_player):
        return self.strategy

    def update_game(self, aGame):
        """ Get a game """
        self.last_game = copy.copy(self.game)
        self.game = aGame

    def name(self):
        return self.strategy_name


class AlwaysCooperate(Strategy):
    """ Always Cooperate Strategy """
    def __init__(self):
        super().__init__()
        self.strategy_name = "always_cooperate"
        self.strategy = "C"


class AlwaysDefect(Strategy):
    """ Never Cooperate Strategy """
    def __init__(self):
        super().__init__()
        self.strategy_name = "always_defect"
        self.strategy = "D"


class RandomPlay(Strategy):
    """ Cooperate randomly """
    def __init__(self):
        super().__init__()
        self.strategy_name = "random"
        self.strategy = ["D", "C"]

    def select_game(self, other_player):
        """ Random Strategy """
        return random.choice(self.strategy)


class SimpleTitForTat(Strategy):
    def __init__(self):
        super().__init__()
        self.strategy_name = "simpleTitForTat"
        self.other_last_strategy = "C"
        self.selected_strategy = "C"

    def select_game(self, other_player):
        """ Simple Tit for tat strategy """
        if self.last_game.other_play == "C":
            self.selected_strategy = "C"
        else:
            self.selected_strategy = "D"

        return self.selected_strategy
    
class TitForTat(Strategy):
    def __init__(self):
        super().__init__()
        self.strategy_name = "TitForTat"
        self.strategy = ["D", "C"]

        self.other_last_strategy = random.choice(self.strategy)
        #self.selected_strategy = random.choice(self.strategy)
        self.selected_strategy = "c"
        self.others = {}

    def update_game(self, aGame):
        """ Get a game """
        self.last_game = copy.copy(self.game)
        self.game = aGame
        self.update_memory(aGame)

    def select_game(self, other_player):
        """ Tit for tat strategy """

        self.recall_games(other_player)
        if self.last_game.other_play == "C":
            self.selected_strategy = "C"
        else:
            self.selected_strategy = "D"

        return self.selected_strategy
    
    def recall_games(self, other_player):
        """ Recall the last play from the opponent"""
        strategy =  ["D", "C"]
        if other_player.name in self.others:
            self.last_game.other_play = self.others[other_player.name]
        else:
            #game = random.choice(["D","C"])
            game = "C"
            self.others[other_player.name] = game
            self.last_game.other_play = game
    
            #self.others[other_player.name] = "C"
            #self.last_game.other_play = "C"
    
            
    def update_memory(self, aGame):
        self.others[aGame.other_name] = aGame.other_play
 


class SimpleRancorous(Strategy):
    """ Simple Rancorous Strategy
        Agente always defects after somebody defects """
    def __init__(self):
        super().__init__()
        self.strategy_name = "simpleRancorous"
        self.other_last_strategy = "C"
        self.selected_strategy = "C"


    def select_game(self, other_player):
        """ Simple Rancorous Strategy """
        if self.last_game.other_play == "D":
            self.selected_strategy = "D"

        return self.selected_strategy
    

class Rancorous(Strategy):
    """ Simple Rancorous Strategy
        Agent always defects after somebody defects 
        Impl: Lucas 2023-10-25
    """
    def __init__(self):
        super().__init__()
        self.strategy_name = "Rancorous"
        self.other_last_strategy = "C"
        self.selected_strategy = "C"
        self.defectors = {}
        self.anyone_defected = False

    def update_game(self, aGame):
        """ Get a game """
        self.last_game = copy.copy(self.game)
        self.game = aGame
        self.update_memory(aGame)

    def select_game(self, other_player):
        """ Rancorous Strategy """
        self.recall_games(other_player)
        
        if self.last_game.other_play == "D":
            self.selected_strategy = "D"
            self.anyone_defected = True
        else:
            self.selected_strategy = "C"
        
        return self.selected_strategy
    
    def recall_games(self, other_player):
        """ Recall the last play from the opponent"""
        
        if other_player.name in self.defectors:
            self.last_game.other_play = "D"
        else:
            self.last_game.other_play = "C"


    def update_memory(self, aGame):

        if aGame.other_play == "D":
            self.defectors[aGame.other_name] = aGame.other_play
