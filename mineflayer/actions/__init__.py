actions_table = {
    'attack': 1,
    'stop_attack': 2,
    'collect_block': 3,
    'collect_food': 4
}

# class Action:

#     def __init__(self):
#         type = ''

#     # def __type__(self):
#     #     return 

def attack(entity):
    return {
        'action': actions_table['attack'],
        'extra_data': {"entity": entity}
    }

def stop_attack():
    return {
        'action': actions_table['stop_attack'],
        'extra_data': {'entity': entity}
    }