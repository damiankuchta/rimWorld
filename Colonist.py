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

    def take_action(self, colony):
        while self.active_actions > 0:
            action = input("chose action for: " + self.name)

            if action == "b":
                self.build(colony)
            elif action == "h":
                self.hunt()
            elif action == "c":
                self.cook()
            elif action == "r":
                self.research()
            elif action == "t":
                self.trade()
            elif action == "hp":
                self.heal()
            elif action == "f":
                self.farm()
            else:
                print("not viable option")

    def add_food_poisoning(self):
        self.status['food_positions'] = colonist_status_food_poisoning_duration

    def eat(self, colony):
        if colony.food["cooked_food"] > 0:
            colony.remove_cooked_food(colonist_eat_cooked_food)
        elif colony.food["raw_food"] > 0:
            colony.remove_raw_food(colonist_eat_raw_food)
        else:
            self.deduct_health(colonist_eat_no_food_health_penalty)
            colony.remove_raw_food(colonist_eat_cooked_food)

            if random() > colonist_eat_chances_of_food_poisoning:
                self.add_food_poisoning()

    def build(self, colony):
        build = input("what building do you want to build? ")
        resources = input("what resources do you want to use?  ")

        building = buildings.get(build, 'invalid')

        if building != 'invalid':
            if building.building_action_cost <= self.active_actions:
                is_sucesfull = colony.add_building(building, resources)
                if is_sucesfull:
                    self.active_actions -= building.building_action_cost
            else:
                print("not enough actions")
        else:
            print("this material is not an option")

    def hunt(self):
        print('hunt')

    def cook(self):
        pass

    def research(self):
        pass

    def trade(self):
        pass

    def heal(self):
        pass

    def farm(self):
        pass
