# -*- coding: utf-8 -*-
""" Prediction Model for the El Farol Problem """

import random
import numpy as np


class PredictionModel:
    """ The prediction model that the agent uses to choose the strategy
        Arthur's paper (1994) strategies
        1. the same as last week's
        2. a mirror image around 50 of last week's
        3. a (rounded) average of the last four weeks
        4. the trend in last 8 weeks, bounded by [0,100]
        5. the same as 2 weeks ago (2-period cycle detector)
        6. the same as 5 weeks ago (5-period cycle detector)
    """

    def __init__(self, agent, recall):
        """ Init the strategy of the agent """
        self.model_name = "no_prediction"
        self.agent = agent
        self.recall = recall
        self.no_of_agents = self.agent.model.no_of_agents()

        self.predictors = {'st_same_lw': self.st_same_lw,
                           # 'st_mirror_50_lw': self.st_mirror_50_lw,
                           'st_round_avg_4w': self.st_round_avg_4w,
                           'st_trend_8w': self.st_trend_8w,
                           'st_same_2w': self.st_same_2w,
                           'st_same_5w': self.st_same_5w}

        self.predictors_fitness = {key: [random.random()]
                                   for key in self.predictors.keys()
                                   }
        self.predictions = {key: [random.randrange(0, self.no_of_agents)]
                            for key in self.predictors.keys()
                            }
        self.fitness_function = FitnessFunction(self)

    def step(self):
        """ get agent step """
        return self.agent.my_step

    def no_of_agents(self):
        """ Returns the number of agents """
        self.no_of_agents = self.agent.model.no_of_agents()
        return self.no_of_agents

    def agent_memory(self):
        """ Returns the agent memory """
        return self.agent.memory

    def make_prediction(self, selected_predictors):
        """ The prediction based on the model """
        for name in selected_predictors:
            prediction = self.predictors[name]()
            self.predictions[name].append(prediction)

    def update_fitness(self, predictors, going, target_no):
        """ Updates the fitness of the predictors """
        for name in predictors:
            fitness = self.get_fitness_of_predictor(name, going, target_no)
            self.predictors_fitness[name].append(fitness)

    def get_fitness_of_predictor(self, predictor_name, going, target_no):
        """ Updates the fitness of one predictor """
        if len(going) < self.recall:
            fitness = self.fitness_function.fitness(going, self.predictions[predictor_name])
        else:
            fitness = self.fitness_function.fitness(going[0:self.recall],
                                                    self.predictions[predictor_name][0:self.recall]
                                                    )

        return fitness

    def get_best_prediction(self):
        """ Get the prediction from the fittest predictor """
        predictors_fitness = self.predictors_fitness
        fittest_predictor = max(predictors_fitness, key=predictors_fitness.get)
        return(self.predictions[fittest_predictor][self.step()])

    def get_best_predictor(self, predictors):
        """ Get the prediction from the fittest predictor """
        max_fitness = max(self.predictors_fitness.values())
        fittest_predictor = max(self.predictors_fitness,
                                key=self.predictors_fitness.get)
        prediction = self.predictions[fittest_predictor]
        return [fittest_predictor, max_fitness, prediction]

    def get_fitness(self, predictor_name):
        """ Get the fitness of one predictor """
        return self.predictors_fitness[predictor_name]

    def st_same_lw(self):
        """ Strategy 1. the same as last week's """
        last = len(self.agent.memory) - 1
        return self.agent.memory[last]

    def st_mirror_50_lw(self):
        """ Strategy 2. a mirror image around 50 of last week's """
        no_of_agents = self.agent.model.no_of_agents()
        last = len(self.agent.memory) - 1
        prediction = no_of_agents - self.agent.memory[last]
        if prediction < 0:
            prediction = 0
        return prediction

    def st_round_avg_4w(self):
        """ Strategy 3. a (rounded) average of the last four weeks """
        recall = len(self.agent.memory)
        if recall < 4:
            return round(np.mean(self.agent.memory))
        else:
            return round(np.mean(self.agent.memory[(recall - 4):]))

    def st_trend_8w(self):
        """ Strategy 4. the trend in last 8 weeks, bounded by [0,100] """
        recall = len(self.agent.memory)

        if recall < 7:
            return round(np.mean(self.agent.memory))
        else:
            return round(np.mean(self.agent.memory[(recall - 7):]))

    def st_same_2w(self):
        """ Strategy 5. the same as 2 weeks ago (2-period cycle detector) """
        recall = len(self.agent.memory)
        if recall < 2:
            return random.randint(0, recall)
        else:
            return self.agent.memory[-2]

    def st_same_5w(self):
        """ Strategy 6. the same as 5 weeks ago (5-period cycle detector) """
        recall = len(self.agent.memory)
        if recall < 5:
            return random.randint(0, recall)
        else:
            return self.agent.memory[-5]


class FitnessFunction:
    """Fitness Function for the el-farol bar model
       following:
       Rand, W., & Stonedahl, F. (2007). The El Farol bar problem and computational effort:
         Why people fail to use bars efficiently. Northwestern University, Evanston, IL.

       f(S,t) = sum_(i=t-L)^(t-1) abs(p(S,i) - a(i))
       Where: p(S,i) is the prediction of strategy S on time i and a(i) is the observed
       attendance on time i and L is the memory reacall lenght.
    """

    def __init__(self, owner):
        """ Fitness Function for the El Farol Bar Model Strategies """
        self.owner = owner

    def fitness(self, observed, predicted):
        """Calculate Strategy fitness """
        fitness = 0
        difference = []

        for psi, ai in zip(predicted, observed):
            difference.append(psi - ai)

        sum_diff = sum([abs(diff) for diff in difference])
        if sum_diff != 0:
            fitness = 1 / sum_diff
        else:
            fitness = 0

        return fitness
