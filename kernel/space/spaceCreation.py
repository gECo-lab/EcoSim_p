# -*- coding: utf-8 -*-
"""
Space Creation

The spaces are created using dependency injection
The definition of the spaces that will be used in the simulation is in the yaml file
"""
import importlib
import sys
import kernel.space.basicSpaces as sp
import dependency_injector.errors as errors
import dependency_injector.providers as providers


""" Spaces are the user implementation of the spaces """


class SpaceCreator(object):
    """
    Space Creator
    This is the general Space class implementation
    Space implemented subclass must be used
    """
    def __init__(self, model, spaces_def):
        """
        The init method for space class creation
        Must be referred in the space subclass creation (using super)
        """
        #self.simulation_folder = simulation_folder
        #sys.path.insert(0, self.simulation_folder)
        self.sps = importlib.import_module("spaces")
        self.spaces = dict()
        self.spaces_model = model
        for space_def in spaces_def:
            self.space_type = space_def['space_type']
            self.space_name = space_def['space_name']
            self.space_variables = space_def['space_variables']
            try:
                a_space = "self.sps" + "." + self.space_type
                self.space_class = eval(a_space)
            except NameError:
                print("class ", self.space_type, " is not defined")
            self.space_Factory = SpaceProvider(self.space_class)
            # refazer a interface da clase espaço - Retirar o action_set
            self.space_Factory.add_args(self.spaces_model,
                                        self.space_name,
                                        self.space_variables)
            try:
                self.new_space = self.space_Factory()
                self.spaces[self.space_name] = self.new_space
            except errors.Error as exception:
                print(exception)
                # <class '__main__.space_Factory'>
                # does not know <'__main__.self.space_name'>


class SpaceProvider(providers.Factory):
    """ Space Provider Class"""
    provided_type = sp.Space
