# -*- coding: utf-8 -*-

"""
Scenario Creation

The Scenarios are created using dependency injection
The definition of the Scenarios that will be used in the simulation are in the json file
"""
import kernel.scenario.basicScenarios as scn


class ScenarioCreator(object):
    """ Scenario Generator - Scenario Implemented Subclass must be used """
    def __init__(self, simulation, model, scenarios_def):
        self.scenarios = dict()
        self.simulation = simulation
        self.model = model
        for scenario_def in scenarios_def:
            self.scenario_type = scenario_def['scenario_type']
            self.scenario_name = scenario_def['scenario_name']
            self.scenario_parameters = scenario_def['scenario_parameters']
            self.scenario_variables = scenario_def['scenario_variables']
            self.agents_init = scenario_def['agents_init']
            try:
                a_scenario = "scn" + "." + self.scenario_type
                self.scenario_class = eval(a_scenario)
            except NameError:
                print("class ", self.scenario_type, " is not defined")

            try:
                self.new_scenario = self.scenario_class(self.simulation,
                                                        self.model,
                                                        self.scenario_name,
                                                        self.scenario_parameters,
                                                        self.scenario_variables,
                                                        self.agents_init)            
                self.scenarios[self.scenario_name] = self.new_scenario
            except NameError:
                print("Class ", scn, " does not know ", self.scenario_name)
