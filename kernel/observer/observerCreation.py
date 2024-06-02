#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Observer
Inspired on datacollection.py from mesa abm
https://mesa.readthedocs.io/en/master/
"""
import kernel.observer.basicObservers as obs


class ObserverCreator(object):
    """ Observer Generator - Observer Implemented Subclass must be used"""
    def __init__(self, model, simulation, observer_def, path_to_results):
        self.model = model
        self.simulation = simulation
        self.path_to_results = path_to_results
        self.observers = {}
        for observer in observer_def:
            self.observer_type = observer['observer_type']
            self.observer_name = observer['observer_name']
            self.observer_agent = observer['observer_agent']
            self.observable_vars = observer['observable_vars']

            self.observer_model = self.model
            self.observer_simulation = self.simulation
            try:
                an_observer = "obs" + "." + self.observer_type
                self.observer_class = eval(an_observer)
            except NameError:
                print("class ", self.observer_type, " is not defined")
            try:
                self.new_observer = self.observer_class(self.observer_name,
                                            self.observer_model,
                                            self.observer_simulation,
                                            self.observer_agent,
                                            self.observable_vars,
                                            self.path_to_results)
                self.observers[self.observer_name] = self.new_observer
            except NameError:
                print("Class ", obs, " does not know ", self.observer_class)