
# colonist start

from utils.resources_utils import resources_list

colonist_start_max_actions = 1
colonist_start_health = 10

# colony starting stats:
start_colony_colonist_amount = 3
start_colony_resources = resources_list(wood=10,
                                        stone=10,
                                        metal=10,
                                        cooked_food=10,
                                        raw_food=0)


# colonist actions
colonist_eat_raw_food = 3
colonist_eat_cooked_food = 1

# Food
colonist_eat_no_food_health_penalty = 1
colonist_eat_chances_of_food_poisoning = 0.5
colonist_status_food_poisoning_duration = 2

# colonist building actions
colonist_buff_building_barracks = 1

building_action_cost = 1
building_barrack_cost = resources_list(wood=1, stone=1, metal=1)
building_barrack_max_colonist = 3

actions = ['build', 'hunt', 'cook', 'research', 'trade', 'heal', 'farm']



