# -*- coding: utf-8 -*-
"""
The space class and the associated classes
"""
from collections import OrderedDict


class Space(object):
    """ The space class """
    def __init__(self, model, name,
                 actions_set_file,
                 action_class,
                 variables = None):
        """ Initialize Space Class """

        self.model = model
        self.name = name
        self.actions_set_file = actions_set_file
        self.action_class = action_class
        self.variables = variables
        self.agents = OrderedDict()

    def create_vars(self):
        """Create Space Vars"""
        if self.variables is not None:
            for name, value in self.variables.items():
                self.__setattr__(name, value)

    def enter(self, agent_name, agent):
        """ An agent enter the a space object """
        if agent_name not in self.agents:
            self.agents[agent_name] = agent

    def exit(self, agent_name):
        """ An agent exits a space object """
        if agent_name in self.agents:
            del self.agents[agent_name]

    def update(self):
        """
        A Space updates its values and execute methods
        This method is impmented by space subclass
        """
        pass
