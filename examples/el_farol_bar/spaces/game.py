# -*- coding: utf-8 -*-
""" El Farol Bar space implementation """

import random

from space.basicSpaces import Space


class EFBGame(Space):
    """ Abstract Market """

    STRATEGY = ['GOING', 'NOT GOING']

    def __init__(self, model, 
                 name, 
                 variables
                 ):
        """ Intialize The el Farol Game """
        super().__init__(model, 
                         name, 
                         variables)

        self.number_of_agents = 0
        self.frequency = [random.randint(0, 100)]

    def step(self):
        """ The the step from schedule """
        self.step = self.model.simulation.schedule.step

    def update(self):
        """ Implemented by subclass - Testing update """
        self.play()

    def play(self):
        """ here the players play the game """
        self.collect_strategies()
        self.notify_frequency()
        # self.show_frequency()

    def collect_strategies(self):
        """ The Space Get the agents decisions """
        frequency = 0
        not_going = 0
        for agent in self.model.mixed_agents():
            agent_strategy = agent.play()
            if agent_strategy == self.STRATEGY[0]:
                frequency += 1
            elif agent_strategy == self.STRATEGY[1]:
                not_going += 1
            else:
                print("Wrong Strategy. Agent: ", agent.name, " Strategy: ", agent_strategy)
        self.frequency.append(frequency)

    def calculate_perc_frequency(self):
        """ Space calculates the frequency of the agents """
        self.number_of_agents = self.model.agents_number()
        self.perc_frequency.append(self.frequency[self.step] / self.number_of_agents)

    def notify_frequency(self):
        """ The space notify the agents about the frequency """
        for agent in self.model.agents.values():
            agent.get_frequency(self.frequency[agent.my_step])

    def show_frequency(self):
        """Show the frequency in the el farol bar"""
        print('This thursday', self.frequency[self.step()],
              ' people are going to the Bar. This represents ',
              self.perc_frequency[self.step()] * 100,
              ' percent of the population'
              )
