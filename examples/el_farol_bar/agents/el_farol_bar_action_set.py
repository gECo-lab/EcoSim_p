# -*- coding: utf-8 -*-
""" Basic Strategy Class implementation """

import random
import numpy as np
from .el_farol_bar_prediction_model import PredictionModel


class Strategy:
    """ Implementation of the strategy class """

    STRATEGY = ['GOING', 'NOT GOING']

    def __init__(self, agent, recall):
        """ Init the strategy of the agent """
        self.agent = agent
        self.recall = recall
        self.strategy_name = "classical"
        self.strategy = self.STRATEGY[0]
        self.target = 0.6
        self.no_of_agents = self.agent.model.no_of_agents()
        self.target_no = round(self.no_of_agents * self.target)
        self.frequency = [0]
        self.prediction_model = PredictionModel(agent, recall)
        # self.set_predictors()
        self.set_all_predictors()

    def set_all_predictors(self):
        """ set all predictors in the model """
        self.predictors = list(self.prediction_model.predictors.keys())

    def set_predictors(self):
        """ Set the predictors for this strategy """
        no_of_predictors = len(self.prediction_model.predictors)
        half_of_predictors = np.int(round(no_of_predictors / 2))
        predictors_to_select = random.sample(range(0, no_of_predictors), half_of_predictors)
        predictors_names = list(self.prediction_model.predictors.keys())
        self.predictors = []
        for predictor_number in predictors_to_select:
            self.predictors.append(predictors_names[predictor_number])

    def select_game(self):
        return self.select_strategy()

    def select_strategy(self):
        self.prediction_model.make_prediction(self.predictors)
        prediction = self.prediction_model.get_best_prediction()

        if prediction > self.target_no:
            self.strategy = self.STRATEGY[1]
        else:
            self.strategy = self.STRATEGY[0]

        return self.strategy

    def get_frequency(self, frequency):
        """ The strategy gets the current frequency in the bar """
        self.frequency.append(frequency)

    def payoff(self, agent_play):
        """ Specialized by subclass """
        step = self.agent.my_step
        self.update_fitness()
        if agent_play == 'GOING':
            if self.frequency[step] >= self.target_no:
                return -1
            else:
                return 1
        else:
            if self.frequency[step] >= self.target_no:
                return 1
            else:
                return -1

    def update_fitness(self):
        """ Updates the payoffs of the strategies """
        self.prediction_model.update_fitness(
            self.predictors,
            self.frequency,
            self.target_no
        )

    def selected_predictor(self):
        """Returns the selected predictor and its fitness """
        return self.prediction_model.get_best_predictor(self.predictors)


class LikeCrowded(Strategy):
    """  Strategy Like Crownded """
    def __init__(self, agent, recall):
        super().__init__(agent, recall)
        self.strategy_name = "likeCrowded"
        self.strategy = self.STRATEGY[0]

    def select_strategy(self):
        """ Like Crownded Strategy """
        self.prediction_model.make_prediction(self.predictors)
        prediction = self.prediction_model.get_best_prediction()

        if prediction > self.target_no:
            self.strategy = self.STRATEGY[0]
        else:
            self.strategy = self.STRATEGY[1]

        return self.strategy


    def payoff(self, agent_play):
        """ Specialized by subclass """
        return random.randint(0,100)


class LikeSixtyPercent(Strategy):
    """ Strategy under sixty percent """
    def __init__(self, agent, recall):
        super().__init__(agent, recall)
        self.strategy_name = "likeSixtyPercent"


class RandomPlay(Strategy):
    """ Strategy under random """
    def __init__(self, agent):
        super().__init__(agent)
        self.strategy_name = "random"

    def select_strategy(self):
        """ Random Strategy """
        return random.choice(self.STRATEGY)
