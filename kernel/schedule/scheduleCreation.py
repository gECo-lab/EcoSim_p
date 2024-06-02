#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Schedule Creation

The schedule is created using dependency injection
The definition of the schedule that will be used in the simulation is in the json file

"""

import kernel.schedule.basicSchedule as schd


class ScheduleCreator(object):
    """ Schedule Generator - Schedule Implemented Subclass must be used """
    def __init__(self, model, schedule_def):
        self.model = model
        for schedule in schedule_def:
            self.schedule_type = schedule['schedule_type']
            self.schedule_name = schedule['schedule_name']
            self.schedule_model = self.model
            try:
                a_schedule = "schd" + "." + self.schedule_type
                self.schedule_class = eval(a_schedule)
            except NameError:
                print("class ", self.schedule_type, " is not defined")
            try:
                self.new_schedule = self.schedule_class(self.schedule_name,
                                                        self.schedule_model)
            except NameError:
                print("Class ", schd, " does not know ", self.schedule_class)
            self.provided_schedule = self.new_schedule