# -*- coding: utf-8 -*-

"""
Simulation Class (This implements a batch simulation)

"""
import json
import sys
import datetime as dt
from model import Model
from scenarioCreation import ScenarioCreator


class Simulation(object):
    """This class implements a simulation"""

    def __init__(self, simulation_config_file, simulation_file):
        """ Initialize a Simulation """
        self.simulation_config = None
        self.json_simulation_defs = None
        self.active_scenario = None

        # Read the simulation configuration file
        with open(simulation_config_file) as read_file:
            self.simulation_config = json.load(read_file)

        # Initialize the simulation from a json file
        with open(simulation_file) as read_file:
            self.json_simulation_defs = json.load(read_file)

        # Get Simulation Paths
        self.path_to_model = self.simulation_config['paths']['model']
        self.path_to_results = self.simulation_config['paths']['results']
        sys.path.insert(0, self.path_to_model)
        self.initialize_simulation()
     
    def initialize_simulation(self):
        """ Factory pattern to create a simulation"""

        # Simulation Name
        self.name = self.json_simulation_defs["simulation_name"]

        # Create Model 
        self.model = Model(self, self.json_simulation_defs, 
                           self.path_to_results)

        # Set Simulation Parameters
        for parameter in self.json_simulation_defs['simulation_parameters']:
            self.parameter_name = parameter['parameter_name']
            self.parameter_value = parameter['parameter_value']
            setattr(self, self.parameter_name, self.parameter_value)

        # Create Scenarios
        self.create_scenarios()

    def create_scenarios(self):
        """ Scenario creation """
        self.scenarios_def = self.json_simulation_defs['scenarios']
        self.scenarios_factory = ScenarioCreator(self, self.model,
                                                 self.scenarios_def)
        self.scenarios = self.scenarios_factory.scenarios

    def execute_simulation(self):
        """
        Executes a Simulation.

        This method gets all scenarios in the json definition and executes
        the defined number of runs for each scenario
        """
        self.pre_simulation()
        for scenario in self.scenarios.values():
            self.active_scenario = scenario
            scenario.execute_scenario()
        self.post_simulation()

    def pre_simulation(self):
        """ Executes routines pre simulation"""
        for space in self.model.spaces.values():
            space.create_vars()



    def post_simulation(self):
        """ Executes the routines post simulation """
        for observer_name, observer in self.model.agent_observers.items():
            observer.create_dataframe()
            self.now = dt.datetime.now().isoformat(timespec='minutes')
            self.filename = "_".join([self.name,
                                     observer_name,
                                      self.now, '.csv'])
            observer.save_dataframe(self.filename)


