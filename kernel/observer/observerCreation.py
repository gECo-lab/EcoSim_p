#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Observer
Inspired on datacollection.py from mesa abm
https://mesa.readthedocs.io/en/master/
"""
import kernel.observer.basicObservers as obs
import dependency_injector.errors as errors
import dependency_injector.providers as providers


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
            self.observer_Factory = ObserverProvider(self.observer_class)
            self.observer_Factory.add_args(self.observer_name,
                                           self.observer_model,
                                           self.observer_simulation,
                                           self.observer_agent,
                                           self.observable_vars,
                                           self.path_to_results)
            try:
                self.new_observer = self.observer_Factory()
                self.observers[self.observer_name] = self.new_observer
            except errors.Error as exception:
                print(exception)
                # <class '__main__.observer_Factory'>
                # does not know <'__main__.self.observer_name'>


class ObserverProvider(providers.Factory):
    """ Observer Provider Class"""
    provided_type = obs.Observer
