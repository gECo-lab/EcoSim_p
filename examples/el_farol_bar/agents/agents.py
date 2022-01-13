# -*- coding: utf-8 -*-
""" Agents for the el farol bar problem """

from agent.basicAgents import DiscreteEventAgent
from .el_farol_bar_action_set import Strategy, RandomPlay, LikeCrowded, LikeSixtyPercent
import random


class Player(DiscreteEventAgent):
    """ A basic player in the El Farol Bar Problem """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.payoff = 0
        self.my_play = ""
        self.other_play = ""
        self.memory = [0]
        self.memory_recall = 10
        self.strategy = Strategy(self, self.memory_recall)
        self.selected_predictor = ""
        self.predictor_fitness = 0.0
        self.predictor_prediction = 0

    def step(self):
        """ agent step """
        self.select_game()

    def select_game(self):
        """ The agent select a play from a strategy """
        self.game_payoff()
        selected_predictor = self.strategy.selected_predictor()
        self.selected_predictor = selected_predictor[0]
        self.predictor_fitness = selected_predictor[1][self.my_step]
        self.predictor_prediction = selected_predictor[2][self.my_step]
        self.my_play = self.strategy.select_game()

    def play(self):
        """ The agent plays a strategy - method my_play """
        return self.my_play

    def game_payoff(self):
        """ Get the game payoff """
        self.payoff = self.strategy.payoff(self.my_play)

    def get_frequency(self, frequency):
        """"Get the frequency in the bar """
        self.memory.append(frequency)
        self.strategy.get_frequency(frequency)


class RandomPlayer(Player):
    """ A player that always defect """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.strategy = RandomPlay(self)

    def select_game(self):
        """Random selection of the game"""
        if random.random() > .5:
            self.my_play = "GOING"
        else:
            self.my_play = "NOT GOING"


class LikeCrowdedPlayer(Player):
    """ A player that always defect """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.strategy = LikeCrowded(self, self.memory_recall)

    def select_game(self):
        """ The agent select a play from a strategy """
        selected_predictor = self.strategy.selected_predictor()
        self.selected_predictor = selected_predictor[0]
        self.predictor_fitness = selected_predictor[1][self.my_step]
        self.predictor_prediction = selected_predictor[2][self.my_step]
        self.my_play = self.strategy.select_game()


class LikeSixtyPercentPlayer(Player):
    """ A player that always defect """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.strategy = LikeSixtyPercent(self, self.memory_recall)
