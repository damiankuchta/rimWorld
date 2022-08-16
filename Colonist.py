from config import colonist_eat_no_food_health_penalty, colonist_eat_chances_of_food_poisoning, \
    colonist_status_food_poisoning_duration, colonist_start_health, \
    colonist_start_max_actions, colonist_eat_raw_food, colonist_eat_cooked_food

from buildings.buildings import buildings
from random import random


class Colonist:
    def __init__(self, name):
        self.name = name
        self.health = colonist_start_health
        self.status = {}
        self.max_actions = colonist_start_max_actions
        self.active_actions = colonist_start_max_actions

    def __str__(self):
        return "NAME " + self.name + " HEALTH: " + str(self.health) + " STATUS: " + str(self.status)

    def deduct_health(self, amount):
        self.health = self.health - amount

    def add_health(self, amount):
        self.health = self.health + amount

    def take_action(self, colony, action, **kwargs):
        if self.active_actions > 0:
            action_func = getattr(self, action)
            return action_func(colony, **kwargs)
        else:
            return [False, "colonist does not have enough actions"]

    def reset_actions(self):
        self.active_actions = self.max_actions

    def add_food_poisoning(self):
        self.status['food_positions'] = colonist_status_food_poisoning_duration

    def eat(self, colony):
        if colony.resources["cooked_food"] > 0:
            colony.remove_cooked_food(colonist_eat_cooked_food)
        elif colony.resources["raw_food"] > 0:
            colony.remove_raw_food(colonist_eat_raw_food)
        else:
            self.deduct_health(colonist_eat_no_food_health_penalty)
            colony.remove_raw_food(colonist_eat_cooked_food)

            if random() > colonist_eat_chances_of_food_poisoning:
                self.add_food_poisoning()

    def build(self, colony, build, resources):
        building = buildings.get(build, 'invalid')

        if building != 'invalid':
            if building.building_action_cost <= self.active_actions:
                is_sucesfull = colony.add_building(building, resources)
                if is_sucesfull[0]:
                    self.active_actions -= building.building_action_cost
                return is_sucesfull
            else:
                return [False, "Not enough action costs"]
        else:
            return [False, "This Building is not an option"]

    def hunt(self, colony, **kwargs):
        print('hunt')

    def cook(self, colony, **kwargs):
        print("cook")

    def research(self, colony, **kwargs):
        print("research")

    def trade(self, colony, **kwargs):
        print("trade")

    def heal(self, colony, **kwargs):
        print("heal")

    def farm(self, colony, **kwargs):
        print("farm")
