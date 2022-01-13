#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the classes that deal 
with the agent vars.

"""

import datetime as dt
import numpy as np


class AgentVarsCreator(object):
    """
        This is the class responsible to create the agent vars.
        It receives the agent vars definitions 
        and create the vars for each scenario.
        This class is controlled by the scenario
    """

    def __init__(self, schedule_name, model, agents_init) -> None:
        self.schedule_name = schedule_name
        self.model = model
        self.agents_init = agents_init
        self.vars_by_agent_type = dict()
        

    def initialize_agents_vars(self):
        """
        The scenario object initializes the 
        variables dict from the yaml agent
        variables  definition (for each scenario)
        """
        # TODO: This probably will need revision - Using agent pool and simply
        # resetting the agents variable will be more efficient
        # TODO: This will probably be better to be as a part of the agent class
        self.vars_by_agent_type = dict()
        for agent_type, agent_vars in self.agents_init.items():
            try:
                if self.model.check_agent_type(agent_type):
                    self.vars_dict = dict()
                    for var in agent_vars:
                        self.agent_var_name = var['var_name']
                        self.agent_var_type = var['var_type']
                        self.agent_var_dist = var['var_dist']
                        self.agent_var_value = var['var_value']
                        self.a_var = AgentVar(self.agent_var_name,
                                         self.agent_var_type,
                                         self.agent_var_dist,
                                         self.agent_var_value)
                        self.vars_dict[self.a_var.name] = self.a_var
                        self.vars_by_agent_type[agent_type] = self.vars_dict
            except KeyError:
                print("There is no agent type called ", agent_type,
                      " in this model")
        # return vars dict
        return self.vars_by_agent_type
            

class AgentVar(object):
    """ An agent var """
    def __init__(self, name, var_type, var_dist, value):
        self.name = name
        self.var_type = var_type
        self.dist = var_dist
        self.value = value
        self.generate_value()

    def generate_value(self):
        """ Generates the value for the 
            agent  stochastic variable 
            using the definition 
            in the variable object 
        """
        if self.var_type == 'stochastic':
            self.value = eval(self.dist)
             
        return self.value

    def set_var_value(self, agent):
        """ Using the variables dict, 
            the scenario object initializes 
            the variables for one agent 
        """
        self.generate_value()
        agent.set_attribute(self.name, self.value)


