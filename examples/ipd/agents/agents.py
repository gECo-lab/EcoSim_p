# -*- coding: utf-8 -*-
""" Agents for the iterated prisioners dilemma model """

from agent.basicAgents import DiscreteEventAgent
from .ipd_action_set import Strategy, AlwaysCooperate, AlwaysDefect, RandomPlay, SimpleTitForTat, Game


class Player(DiscreteEventAgent):
    """ A basic player in the Iterated Prisioners Dilemma """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.my_payoff = 0
        self.my_play = "C"
        self.other_name = ""
        self.other_play = "C"
        self.other_payoff = 0
        self.strategy = Strategy()
        self.game = Game(self.name, "C", 3, "", "C", 3)
        self.strategy.update_game(self.game)

    def step(self):
        """ The agent selects a play from a strategy """
        self.my_play = self.strategy.select_game()

    def play(self):
        """ The agent plays a strategy """
        return self.my_play

    def game_payoff(self, other_name, other_play, other_payoff, my_payoff):
        """ Get the game payoff """
        self.my_payoff = my_payoff
        self.other_name = other_name
        self.other_play = other_play
        self.other_payoff = other_payoff
        self.game.my_payoff = my_payoff
        self.game.other_name = other_name
        self.game.other_play = other_play
        self.game.other_payoff = other_payoff
        self.strategy.update_game(self.game)
        # print("ag name: ", self.name, "play: ", self.my_play, "payoff: ", self.my_payoff)


class GoodPlayer(Player):
    """ A player that always cooperate """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.strategy = AlwaysCooperate()


class BadPlayer(Player):
    """ A player that always defect """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.strategy = AlwaysDefect()


class RandomPlayer(Player):
    """ A player that always defect """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.strategy = RandomPlay()


class TitForTatPlayer(Player):
    """ A player that always defect """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.strategy = SimpleTitForTat()
