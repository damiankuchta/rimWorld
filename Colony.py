
from Colonist import Colonist
from config import start_colony_resources, start_colony_colonist_amount


class Colony:
    def __init__(self):
        self.resources = start_colony_resources
        self.colonists = [Colonist(name='dummy'), Colonist(name='dummy'), Colonist(name='dummy')] # * start_colony_colonist_amount
        self.buildings = []

    def __str__(self):
        return 'colony'

    def remove_cooked_food(self, amount):
        self.resources['cooked_food'] -= amount

    def remove_raw_food(self, amount):
        self.resources['raw_food'] -= amount

    def feed_colonist(self):
        for c in range(len(self.colonists)):
            self.colonists[c].eat(colony=self)

    def add_building(self, building, resources):
        if resources in building.cost.keys():
            if self.resources[resources] >= building.cost[resources]:
                self.resources[resources] -= building.cost[resources]
                building.set_material_used(resources)
                self.buildings.append(building)
                return [True, ""]
            return [False, "not enough resources"]
        return [False, 'cannot build with this type of resources']

    def reset_actions(self):
        for c in range(len(self.colonists)):
            self.colonists[c].reset_actions()

    def reset(self):
        self.feed_colonist()
        self.reset_actions()








