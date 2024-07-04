# -*- coding: utf-8 -*-
"""
Definition of the class Observer
"""

import datetime as dt

import pandas as pd


class Observer(object):
    """
    The observer classs - This class observe the agents and collects data
    """

    def __init__(self, name, model, simulation, entity_class, agent_vars, path_to_results):
        """ Initialize the observer class """
        self.name = name
        self.model = model
        self.simulation = simulation
        self.schedule = model.schedule
        self.observable_entity = entity_class
        self.agent_observables = {}
        self.agent_observation = {}
        self.observables_keys = {}
        self.observation_keys = {}
        self.obs_no = 0
        self.filename = None
        self.add_observables_keys()
        self.observation = None
        self.agent_vars = agent_vars
        self.define_observable_vars()
        self.observables = None
        self.create_observables()
        self.path_to_results = path_to_results
        self.first = True

    def define_observable_entity(self, entity_class):
        """ Defines the type of agent that will be observed by this observer """
        if entity_class not in self.model.dir():
            raise ValueError('{entity_class} not defined in the current scope')
        self.observable_entity = entity_class

    def add_observables_keys(self):
        """
        Add general observable variables from the agent (model, simulation, scenario, run, step, time, agent_name)
        """
        self.observables_keys = {'model': [self.model.name],
                                 'simulation': [self.simulation.name],
                                 'observer':[self.name],
                                 'scenario': [self.schedule.scenario_name],
                                 'run': [0],
                                 'step': [0],
                                 'time': [dt.datetime.now().isoformat(timespec='minutes')],
                                 'agent_name': [' ']}

    def update_observation_keys(self):
        """ Updates the general observable variables at each observation (step) """
        self.observation_keys['model'] = self.model.name
        self.observation_keys['simulation'] = self.simulation.name
        self.observation_keys['observer'] = self.name
        self.observation_keys['scenario'] = self.schedule.scenario_name
        self.observation_keys['run'] = self.schedule.run_nr
        self.observation_keys['step'] = self.step
        self.observation_keys['time'] = dt.datetime.now().isoformat(timespec='minutes')

    def define_observable_vars(self):
        """ Define the variables that observe will update in the observation (defined in the yaml file) """
        if self.observable_entity is not None:
            for var in self.agent_vars:
                self.agent_observables[var] = [0]
                self.agent_observation[var] = " "
        else:
            raise ValueError('{observable_entity} not defined')

    def basic_observation(self):
        """ Observer the agent variables """
        self.observation = None
        agents_to_observe = self.model.agents_of_type(self.observable_entity)
        self.update_observation_keys()
        for agent_name, agent in agents_to_observe.items():
            self.observation_keys['agent_name'] = agent_name
            for agent_var_name in self.agent_observables.keys():
                self.agent_observation[agent_var_name] = getattr(agent, agent_var_name)
            self.observation = {**self.observation_keys, **self.agent_observation}
            if self.first:
                self.set_observation()
                self.first = False
            else:
                self.append_observation()

    def create_observables(self):
        """ Create the dictionary of observable variables (for the observation file) """
        self.observables = {**self.observables_keys, **self.agent_observables}

    def append_observation(self):
        """ Append an observation in the observables dictionary """
        for var, value in self.observables.items():
            value.append(self.observation[var])
    
    def set_observation(self):
        """ Set an observation in the observables dictionary """
        for var, value in self.observables.items():
            value[0] = self.observation[var]


    def create_dataframe(self):
        self.observations = pd.DataFrame(self.observables)

    def save_dataframe(self, df_name):
        """  Create a dataframe to update the observations """
        self.filename = self.path_to_results + df_name
        self.observations.to_csv(self.filename, index_label='index_no')

    def observe(self, step):
        """ Observe the variables """
        self.step = step
        self.basic_observation()
