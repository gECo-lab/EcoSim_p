#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Scenario
"""
# TODO: Incorporar a reinicialização dos agentes a cada "run"
# TODO: Revisar o tratamento de acesso aos agentes 
# (sincronizado com o dicionario "agents" do modelo)


import datetime as dt
import concurrent.futures
import numpy as np
# import yappi #using to profile code

from  agent.agentVars import AgentVarsCreator


class Scenario(object):
    """
   Class that contains
    the definitions of a scenario
    """
    def __init__(self, simulation, model, name,
                 parameters, variables, agents_init):
        """Initialize a Scenario (with yaml definitions) """
        self.simulation = simulation
        self.model = model
        self.name = name
        self.parameters = parameters
        self.variables = variables
        self.agents_init = agents_init
        
        self.initialize_parameters()
        self.initialize_variables()

        self.vars_generator = AgentVarsCreator(self.name, 
                                        self.model,
                                        self.agents_init
                                        )


    def initialize_parameters(self):
        """
        Initialize the scenario parameters
        The parameters (names and values) 
        come from scenario json definition
        """
        for parameter in self.parameters:
            self.parameter_name = parameter['parameter_name']
            self.parameter_value = parameter['parameter_value']
            setattr(self, self.parameter_name, self.parameter_value)

    def initialize_variables(self):
        """
        Initialize scenario variables
        The scenario variables come from the yaml scenario definition
        """
        for variable in self.variables:
            self.variable_name = variable['var_name']
            self.variable_value = variable['var_init_value']
            setattr(self, self.variable_name, self.variable_value)

    def initialize_schedule(self):
        """ Initialize the schedule depending on type of schedule """
        self.schedule = self.model.schedule

    def execute_scenario(self):
        """
        Execute the scenario
        The simulation executes an pre-scenario and a post-scenario for each scenario
        """
        # yappi.start() # init profiling
        self.pre_scenario()
        for run_nr in range(self.no_of_runs):
            if self.reset_each_run:
                self.pre_run()
            self.run(run_nr)
            # fstats = yappi.get_func_stats()   # get statistics
            # fstats.print_all()
            # tstats = yappi.get_thread_stats()
            # tstats.print_all()
        self.post_scenario()
        # fstats = yappi.get_func_stats()   # get statistics
        # fstats.print_all()
        # tstats = yappi.get_thread_stats()
        # tstats.print_all()

    def pre_scenario(self):
        """ Initializes the scenario parameters, 
        variable, shcedule, agents vars etc. """
        self.initialize_parameters()
        self.initialize_variables()
        self.initialize_schedule()
        self.create_agents()
        self.vars_generator_dict = self.vars_generator.initialize_agents_vars()
        self.initialize_agents()

    def pre_run(self):
        """ Initializes the scenario parameters, 
            variable, schedule, agents vars etc. 
        """
        self.create_agents()
        self.initialize_agents()
            
    def run(self, run_nr):
        """
        This method executes the schedule
        """
        # Needs to change to be generic and depedent on the type of scheduling
        self.schedule.execute(self.name,
                              self.step_unit,
                              self.step_interval,
                              self.no_of_steps,
                              run_nr)

    def run_threaded(self, run_nr):
        """
        This method executes the schedule
        """
        # Needs to change to be generic and depedent on the type of scheduling
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(self.schedule.execute,
                            self.name,
                            self.step_unit,
                            self.step_interval,
                            self.no_of_steps,
                            run_nr)

    def post_scenario(self):
        """
        In post scenario, the  observation dataframe is saved
        """
        # TODO: Review observer dataframe writing methods (big dataframe consume ram)
        #for observer_name, observer in self.model.agent_observers.items():
        #    observer.create_dataframe()
        #    self.now = dt.datetime.now().isoformat(timespec='minutes')
        #    self.filename = "_".join([self.simulation.name,
        #                             observer_name,
        #                              self.now, '.csv'])
        #    observer.save_dataframe(self.filename)

    def create_agents(self):
        """The scenario orders model to create the agents"""
        self.model.create_agents()
        for agent in self.model.agents.values():
            agent.scenario = self
    
    def initialize_agents(self):
        """Initialize the agents """
        #self.vars_generator_dict = self.vars_generator.initialize_agents_vars()
        for agent_type, agent_vars in self.vars_generator_dict.items():
            for agent  in self.model.agents_of_type(agent_type).values():
                self.init_an_agent_vars(agent, agent_vars)

    def init_an_agent_vars(self, agent, agent_vars):
        """Init the vars of an agent """
        for var in agent_vars.values():
            var.set_var_value(agent)

    def initialize_one_agent_vars(self, agent_type, agent):
        """ Initialize the vars of one agent """
        agent_vars = self.vars_generator_dict[agent_type]
        self.init_an_agent_vars(agent, agent_vars)

    def initialize_one_var(self, var_name, agent_type, agent):
        """ Initialize the vars of one agent """
        agent_var = self.vars_generator_dict[agent_type][var_name]
        agent_var.set_var_value(agent)
