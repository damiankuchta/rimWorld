from config import building_barrack_cost, building_barrack_max_colonist, building_action_cost
from resources import building_resources


class Barrack:
    def __init__(self):
        self.cost = building_barrack_cost
        self.name = "Barrack"
        self.benefits = {"colonist": {"actions": 1}}
        self.assigned_to = []
        self.max_colonist = building_barrack_max_colonist
        self.building_action_cost = building_action_cost
        self.material_used = ''

    def __str__(self):
        return 'Barracks'

    def __repr__(self):
        return 'Barracks('+self.material_used+")"

    def how_many_empty_spaces(self):
        print("you can put " + str(self.max_colonist - len(self.assigned_to)) + " colonist")

    def assign_colonist(self, colonist_id):
        if self.max_colonist > len(self.assigned_to):
            self.assigned_to.append(colonist_id)
        else:
            print("not enough spaces!")

    def remove_colonist(self, colonist_id):
        if colonist_id in self.assigned_to:
            self.assigned_to.remove(colonist_id)
        else:
            print("colonist no assigned!")

    def set_material_used(self, material):
        if material in building_resources:
            self.material_used = material
        else:
            print("material not existent")



