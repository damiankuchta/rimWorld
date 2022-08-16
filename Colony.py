
from Colonist import Colonist
from config import start_colony_resources, start_colony_raw_food, \
    start_colony_cooked_food, start_colony_colonist_amount


class Colony:
    def __init__(self):
        self.food = {
            'cooked_food': start_colony_cooked_food,
            'raw_food': start_colony_raw_food,
        }
        self.resources = start_colony_resources
        self.colonists = [Colonist(name='dummy')] * start_colony_colonist_amount
        self.buildings = []

    def __str__(self):
        print(str(self.food) + '\n' + str(self.resources) + "\n" + str(self.buildings))
        for c in range(len(self.colonists)):
            print(self.colonists[c])
        return ""

    def remove_cooked_food(self, amount):
        self.food['cooked_food'] = self.food['cooked_food'] - amount

    def remove_raw_food(self, amount):
        self.food['raw_food'] = self.food['raw_food'] - amount

    def feed_colonist(self):
        for c in range(len(self.colonists)):
            self.colonists[c].eat(colony=self)

    def take_actions(self, colony):
        for c in range(len(self.colonists)):
            self.colonists[c].take_action(colony)

    def add_building(self, building, resources):
        if resources in building.cost.keys():
            if self.resources[resources] >= building.cost[resources]:
                self.resources[resources] -= building.cost[resources]
                building.set_material_used(resources)
                self.buildings.append(building)
                return True
            else:
                print("not enough resources")
        else:
            print('cannot build with this type of resources')
        return False






