# -*- coding: utf-8 -*-
"""
Agent Creation

The agents are created using dependency injection
The definitions of the agents that will be used in the simulation are in the yaml file
"""
import importlib
import sys
import dependency_injector.errors as errors
import dependency_injector.providers as providers

""" agents are the user implementation of the agents """
#from ..agents import agents as ag


class AgentPopulationCreator(object):
    """
    Agent Population Generator
    Agent Implemented Subclass must be used
    """
    def __init__(self, simulation, model, agents_def):
        self.agents_module = simulation.path_to_model + "agents"
        self.agents_package = model.name
        self.ag = importlib.import_module("agents")
        #print(self.ag)
        self.agents = dict()
        self.agents_by_type = dict()
        self.agents_simulation = simulation
        self.agents_model = model
        for agent_def in agents_def.values():
            self.agent_type = agent_def['agent_type']
            self.agent_prefix = agent_def['agent_prefix']
            self.agent_population_size = int(agent_def['no_of_agents'])
            try:
                an_agent = "self.ag" + "." + self.agent_type
                self.agent_class = eval(an_agent)
                # print(self.agent_class)
                self.agents_by_type[self.agent_type] = dict()
            except NameError:
                print("class ", self.agent_type, " is not defined")
            for agent_number in range(self.agent_population_size):
                self.agent_Factory = AgentProvider(self.agent_class)
                self.agent_name = self.agent_prefix + '_' + str(agent_number)
                self.agent_Factory.add_args(self.agents_simulation,
                                            self.agents_model,
                                            agent_number,
                                            agent_def)
                try:
                    self.new_agent = self.agent_Factory()
                    self.agents[self.agent_name] = self.new_agent
                    self.agents_by_type[self.agent_type][self.agent_name] = self.new_agent
                except errors.Error as exception:
                    print(exception)
                    # <class '__main__.agent_Factory'>
                    # does not know <'__main__.self.agent_name'>
        

class AgentCreator(object):
    """
    Agent Generator
    Agent Implemented Subclass must be used
    """
    def __init__(self, simulation, model, an_agent_def, agent_number):
        self.ag = importlib.import_module("agents")
        self.an_agent_simulation = simulation
        self.an_agent_model = model
        
        self.agent_type = an_agent_def['agent_type']
        self.agent_prefix = an_agent_def['agent_prefix']
        try:
            an_agent = "self.ag" + "." + self.agent_type
            self.agent_class = eval(an_agent)
        except NameError:
            print("class ", self.agent_type, " is not defined")
        self.agent_Factory = AgentProvider(self.agent_class)
        self.agent_name = self.agent_prefix + '_' + str(agent_number)
        self.agent_Factory.add_args(self.an_agent_simulation,
                                    self.an_agent_model,
                                    agent_number,
                                    an_agent_def)
        try:
            self.new_agent = self.agent_Factory()
        except errors.Error as exception:
            print(exception)
            # <class '__main__.agent_Factory'>
            # does not know <'__main__.self.agent_name'>
        

class AgentProvider(providers.Factory):
    """ Agent Provider Class"""
