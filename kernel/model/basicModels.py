# -*- coding: utf-8 -*-

"""
Definition of the class Model

This class receives a json file with the definition 
of the simulation scenario and then creates the simulation 
with all simulation objects

"""
# TODO: Revisar o dicionario dos agentes. 
# Incorporar no modelo o tratamento de agentes "mortos" (dicionario agents)

import random as rnd
import time
from collections import OrderedDict


from kernel.agent.agentCreation import AgentPopulationCreator, AgentCreator
from kernel.observer.observerCreation import ObserverCreator
from kernel.schedule.scheduleCreation import ScheduleCreator
from kernel.space.spaceCreation import SpaceCreator


class Model:
    """
    Model Basic Class
    Receives the json file name and read it
    Creates all objects in the Simulation
    """

    def __init__(self, simulation, json_model_defs, path_to_results):
        """Load the definitions of the json file"""
        self.seed = time.time()
        self.random = rnd.Random(self.seed)
        self.simulation = simulation
        self.json_defs = json_model_defs

        self.name = self.json_defs['model_name']
        self.schedule_def = self.json_defs['schedule']

        self.spaces = dict()
        self.agents = dict()
        self.agents_by_type = dict()
        self.agent_observers = dict()

        self.create_schedule(self.schedule_def)
        self.create_spaces()
        self.create_observers(path_to_results)


    def create_schedule(self, schedule_def):
        """ Creates the model schedule using the json schedule definition """
        self.schedule_factory = ScheduleCreator(self,
                                                schedule_def)
        self.schedule = self.schedule_factory.provided_schedule

    def create_spaces(self):
        """ Access SpaceFactory (SpaceCreator) and create space objects
            for the simulation from the json definition
        """
        self.spaces_def = self.json_defs['spaces']
        self.spaces_factory = SpaceCreator(self, self.spaces_def)
        self.spaces = self.spaces_factory.spaces
        
    def create_agents(self):
        """
        Access the AgentFactory (AgentPopulationCreator).
        Create the agents
        """
        self.agents_def = self.json_defs['agents']
        self.agents_pop = AgentPopulationCreator(self.simulation, self,
                                                 self.agents_def)

        self.agents = self.agents_pop.agents
        self.agents_by_type = self.agents_pop.agents_by_type

    def create_one_agent(self, agent_type):
        """
        Create one agent and include it in the model
        """
        try:
            self.an_agent_def = self.json_defs['agents'][agent_type]
        except KeyError:
            print(agent_type, ' not defined in the json file')

        self.an_agent_number = self.agents_of_type_number(agent_type) + 1
        
        self.an_agent_creator = AgentCreator(self.simulation, self,
                                                 self.an_agent_def,
                                                 self.an_agent_number)    
        self.new_agent = self.an_agent_creator.new_agent
        self.simulation.active_scenario.initialize_one_agent_vars(agent_type,self.new_agent)
        self.enter_model(self.new_agent.name, self.new_agent)


    def create_observers(self, path_to_results):
        """
        Access the ObserverFactory (ObserverCreator).
        Create the Observers
        """
        self.agent_observers = {}
        self.agent_observers_def = self.json_defs['observers']
        self.agent_observers_pop = ObserverCreator(self, self.simulation,
                                                   self.agent_observers_def, path_to_results)
        self.agent_observers = self.agent_observers_pop.observers
        

    def enter_model(self, agent_name, agent):
        """ An agent enters the model (is included in agents dict) """
        #if agent_name not in self.agents:
        self.agents[agent_name] = agent

        if agent.type not in self.agents_by_type:
            self.agents_by_type[agent.type] = dict()
        self.agents_by_type[agent.type][agent_name] = agent


    def exit_model(self, agent_name):
        """ An agent exits the model (is deleted from agents dict) """
        try:
            agent = self.agents.pop(agent_name)
            del self.agents_by_type[agent.type][agent_name]
        except KeyError:
            print("There is no agent named", agent_name,
                  " in the model ")

    def agents_of_type(self, agent_type):
        """ Returns a dict with the agents with an specific type """
        # TODO: Check this method
        return self.agents_by_type[agent_type]
        #return {key: value for key, value in self.agents.items()
        #        if value == agent_type}

    # def agents_by_type(self):
    #     """ Returns a dict with all agents in the simulation
    #         ordered by type (agent specific class)
    #     """
    #     return OrderedDict({value.__class__.__name__ + "_" + str(key): value
    #                         for key, value in self.agents.items()})

    def agents_number(self):
        """ Returns how many agents we have in the simulation (size of agents dict) """
        return len(self.agents)

    def no_of_agents(self):
        """ Returns how many agents we have in the simulation (size of agents dict) """
        return len(self.agents)

    def agents_of_type_number(self, agent_type):
        """ Returns how many agents of an specific type """
        return len(self.agents_by_type[agent_type])
    
    def check_agent_type(self, agent_type):
        """ Returns true if the agent type exists in the agents_by_type dict """
        return (agent_type in self.agents_by_type)

    def mixed_agents(self):
        """ Returns a randomly shuffled list of agents (from agents dict) """
        agents_names = list(self.agents.keys())
        self.random.shuffle(agents_names)

        for agent_name in agents_names:
            if agent_name in self.agents:
                yield self.agents[agent_name]

    def mixed_spaces(self):
        """ Returns a randomly shuffled list of spaces (from spaces dict) """
        spaces_names = list(self.spaces.keys())
        self.random.shuffle(spaces_names)

        for space_name in spaces_names:
            if space_name in self.spaces:
                yield self.spaces[space_name]
