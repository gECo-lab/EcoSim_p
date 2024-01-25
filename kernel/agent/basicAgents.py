# -*- coding: utf-8 -*-
"""
Definition of the class Agent
"""


class Agent(object):
    """ This is the basic agent class"""
    def __init__(self, simulation, model, agent_number, agent_def):
        """ Agent Initialization from the yaml file
        """
        self.type = agent_def['agent_type']
        self.name = agent_def['agent_prefix'] + '_' + str(agent_number)
        self.simulation = simulation
        self.model = model
        self.active_scenario = self.simulation.active_scenario
        self.spaces = dict()
        self.alive = True
        self.model.enter_model(self.name, self)
        for space_name in agent_def['agent_spaces']:
            try:
                self.enter_space(space_name)
            except KeyError:
                print("There is no space called ", space_name,
                      " in this model")

    def enter_space(self, space_name):
        """ Agent enter space """
        self.model.spaces[space_name]
        self.spaces[space_name] = self.model.spaces[space_name]
        self.spaces[space_name].enter(self.name, self)

    def get_attribute(self, attribute_name):
        """ Get an agent attribute"""
        try:
            this_attribute = None
            this_attribute = self.__getattribute__(attribute_name)
        except AttributeError:
            print("There is no attribute called ", attribute_name,
                  " in agent ", self.name)
        else:
            return this_attribute

    def set_attribute(self, attribute_name, atribute_value):
        """ Set an agent attribute"""
        self.__setattr__(attribute_name, atribute_value)

    def alive(self):
        """ Agent set to alive """
        self.alive = True

    def dead(self):
        """ Agent set to dead """
        self.alive = False
        self.model.exit_model(self.name)

    def executionLoop(self):
        """ An Agent execution loop """
        while self.alive:
            self.step()

    def step(self):
        """ Agent standard step - can be specialized by subclass """
        pass


class DiscreteEventAgent(Agent):

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Discrete Event Agent Initialization
        """
        super().__init__(simulation, model, agent_number, agent_def)
        self.my_step = 0

    def my_step(self):
        """ Returns the agent step """
        return self.my_step

    def dev_step(self, this_step):
        """ Discrete Event Step - Updates the step for the agent """
        self.my_step = this_step
        if self.alive:
            self.step()
       
    def step(self):
        """ Dev Agent standard step - can be specialized by subclass
            -- The code below is only an example
        """
        # Implemented by subclass
        # self.my_step = this_step
        # for action in self.actions.values():
        #     action(self.my_step)
        pass


class EventAgent(Agent):

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Agent Initialization """
        super().__init__(simulation, model, agent_number, agent_def)
        self.my_step = 0
        self.an_event = None

    def step(self, this_step):
        """ Agent standard step - can be specialized by subclass ]
            -- The code below is only an example
        """
        self.my_step = this_step
        for a_space in self.spaces.values():
            for action in a_space.actions.values():
                self.an_event = Event(self, self, action)
                self.an_event.set_status('active')
                a_space.schedule.collect_event(self.an_event)

        #  action(self.my_step)

    # def set_memory(self, a_memory=None):
    #     if a_memory is None:
    #         self.memory = Memory(self)
    #     else:
    #         self.memory = a_memory

    # def set_decision_mechanism(self, a_decision_mechanism=None):
    #     if a_decision_mechanism is None:
    #         self.decision_mechanism = Decision_Mechanism(self)
    #     else:
    #         self.decision_mechanism = a_decision_mechanism

    # def update_event(self, event):
    #     """ Update agent memory """
    #     self.memory.update_event(event)

    # def acts(self, an_event):
    #     # Precisa reduzir o acoplamento aqui
    #     an_event.set_status('active')
    #     self.spaces[an_event.space_name].collect_event(an_event)

    # def create_event(self, an_action):
    #     return Event(self, self.a_space, an_action)
