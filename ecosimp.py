# -*- coding: utf-8 -*-

"""
Model Creation

This method reads a json file, creates de Simulation object
The simulation object has all classes and specifications to 
execute de simulation.
The agents, schedule, spaces, observers, scenarios, initial 
values (for the scenarios) are all defined in the yaml file
After the simulation object is created, the simulation is 
executed (all scenarios, and all runs in each scenario)
The results of the scenarios are writen in files in the 
folder runs
"""
# TODO: Generalize the location specs for the simulation 
#       results files (actually in the folder runs)

import sys
from kernel.simulation import Simulation


def new_simulation(app_dir, model_defs, scenarios_defs):
    """ This is the main simulation method 
        without a graphical interface.
        This method receives 3 parameters:
         - model_config - The configuration file for the model tha
           is executing
         - model_defs - The model definition file name
         - scenario_defs - The scenarios definition file name
    """

    new_sim = Simulation(app_dir, model_defs, scenarios_defs)

    new_sim.execute_simulation()


if __name__ == "__main__":

    app_dir = str(sys.argv[1])
    model_defs = str(sys.argv[2])
    scenarios_defs = str(sys.argv[3])
    new_simulation(app_dir, model_defs, scenarios_defs)
