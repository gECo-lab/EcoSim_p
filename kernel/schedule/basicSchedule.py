# -*- coding: utf-8 -*-
"""
Definition of the class Schedule
"""
from tqdm import trange


class Schedule(object):
    """ Schedule Class """

    def __init__(self, name, model):
        """ Initialize the schedule"""
        self.name = name
        self.model = model
        self.scenario_name = " "

    def execute(self, scenario_name,
                step_unit,
                step_interval,
                no_of_steps,
                run_nr):
        """ Interface for executing methods of schedule objects
            Implemented by subclass
        """
        raise NotImplementedError("Must subclass me")


# TODO: Definir a EventSchedule
# TODO: Eventualmente, implementar o Agente para diferentes tipos de schd
# TODO: Montar um modelo macroeconômico básico (Usando Hilder)


class EventSchedule(Schedule):
    """ An Event Schedule """
    def __init__(self, name, model):
        """ PoolSchedule initialization """
        super().__init__(name, model)
        self.events = dict()

    def collect_event(self, an_event):
        self.events[an_event.event_id] = an_event

    def execute(self, scenario_name,
                step_unit,
                step_interval,
                no_of_steps,
                run_nr):
        pass


class PoolSchedule(Schedule):
    """ A pool schedule """
    def __init__(self, name, model):
        """ PoolSchedule initialization """
        super().__init__(name, model)
        self.run_nr = " "
        self.step = 0

    def execute(self, scenario_name,
                step_unit,
                step_interval,
                no_of_steps,
                run_nr):
        """ Executes the Pool Schedule """
        self.run_nr = run_nr
        self.scenario_name = scenario_name
        self.status = "Scenario: " + self.scenario_name + " Run nr.: " + str(self.run_nr)        
        if step_unit == 'step':
            for this_step in trange(0, no_of_steps, step_interval, desc = self.status):
                self.step = this_step
                for agent_name, agent in self.model.agents.items():
                    agent.dev_step(self.step)
                for space_name, space in self.model.spaces.items():
                    space.update()
                for observer_name, observer in self.model.agent_observers.items():
                    observer.observe(self.step)
        else:
            raise Exception(step_unit,
                            "is not valid as step unity")


class MixedSchedule(Schedule):
    """ A mixed schedule for random execution"""
    def __init__(self, name, model):
        """ Mixed schedule initialization """
        super().__init__(name, model)
        self.run_nr = " "

    def execute(self, scenario_name,
                step_unit,
                step_interval,
                no_of_steps,
                run_nr):
        """ Executes the Mixed Schedule """
        self.run_nr = run_nr
        self.scenario_name = scenario_name
        self.status = "Scenario: " + self.scenario_name + " Run nr.: " + str(self.run_nr)
        if step_unit == 'step':
            for this_step in trange(0, no_of_steps, step_interval, desc=self.status):
                self.step = this_step
                for agent in self.model.mixed_agents():
                    agent.dev_step(this_step)
                for space in self.model.mixed_spaces():
                    space.update()
                for observer_name, observer in self.model.agent_observers.items():
                    observer.observe(this_step)
        else:
            raise Exception(step_unit,
                            "is not valid as step unity")
