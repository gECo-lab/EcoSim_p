# -*- coding: utf-8 -*-

"""
Simulation Class (This implements a batch simulation)

"""


## TODO: Reimplement depebdency injection

import json
import sys
import datetime as dt
from kernel.scenario.scenarioCreation import ScenarioCreator
from kernel.model.basicModels import Model



class Simulation(object):
    """This class implements a simulation"""

    def __init__(self, simulation_config_file, model_file, scenarios_file):
        """ Initialize a Simulation """
        self.simulation_config = None
        self.json_model_defs = None
        self.json_scenarios_defs = None 
        self.active_scenario = None

        # Read the simulation configuration file
        with open(simulation_config_file) as read_file:
            self.simulation_config = json.load(read_file)

        # Initialize the model from a json file
        with open(model_file) as read_file:
            self.json_model_defs = json.load(read_file)

        # Initialize the simulation from a json file
        with open(scenarios_file) as read_file:
            self.json_scenarios_defs = json.load(read_file)

        # Get Simulation Paths
        self.path_to_model = self.simulation_config['paths']['model']
        self.path_to_results = self.simulation_config['paths']['results']
        sys.path.insert(0, self.path_to_model)
        self.initialize_simulation()
     
    def initialize_simulation(self):
        """ Factory pattern to create a simulation"""

        # Simulation Name
        self.name = self.json_model_defs["simulation_name"]
        self.agents_list = self.json_model_defs['agents']
        self.agents_init_dict = self.json_scenarios_defs["scenarios"][0]["agents_init"]


        # Generates the observers definition list
        self.generate_observers_def()

        # Select from the scenario file the agents that will be created
        self.generate_agents_to_create()

        # Create Model 
        self.model = Model(self, self.
                           json_model_defs,
                           self.observers_def_list,
                           self.agents_to_create, 
                           self.path_to_results)
        
        # Create Scenarios
        self.create_scenarios()

    
    def generate_agents_to_create(self):

        self.agents_to_create = []

        for an_agent in self.agents_list:
            agent_class = an_agent["agent_type"]
            if self.agents_init_dict.get(agent_class) is not None:
                self.agents_to_create.append(agent_class)
                


    def generate_observers_def(self):
        """Generates the observers definition list

        """
        self.observers_def_list = []
        self.agent_observable_var = []

        for an_agent in self.agents_list:
            if an_agent["has_observer"]:
                observer_name = an_agent["agent_type"] + "_obs"
                observer_agent = an_agent["agent_type"]
              
                an_agent_obs_vars = self.agents_init_dict.get(observer_agent)
                self.obs_vars = []
                if an_agent_obs_vars is not None:                                     
                    for var in an_agent_obs_vars:
                        if var["observed"]:
                            self.obs_vars.append(var["var_name"])

                    self.an_observer_def = {"observer_type": "Observer",
                                            "observer_name": observer_name,
                                            "observer_agent": observer_agent,
                                            "observable_vars": self.obs_vars
                                            }
                    self.observers_def_list.append(self.an_observer_def)




        return self.observers_def_list






    def create_scenarios(self):
        """ Scenario creation """
        self.scenarios_def = self.json_scenarios_defs['scenarios']
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


