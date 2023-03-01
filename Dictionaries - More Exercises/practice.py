class Dragon:
    """
    This class represents the stats of dragon objects
    """
    def __init__(self, type: str, name: str, damage: int, health: int, armor: int):
        self.type = type
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor

    def add_dragon(self):
        """
        Adds a new Dragon to the list of Dragons or update the list with new stats of existing dragon.
        """
        if self.type not in dragon_army.keys():
            dragon_army[self.type] = {}
            if self.name not in dragon_army[self.type].keys():
                dragon_army[self.type][self.name] = []
                dragon_army[self.type][self.name].append(self.damage)
                dragon_army[self.type][self.name].append(self.health)
                dragon_army[self.type][self.name].append(self.armor)
            else:
                dragon_army[self.type][self.name][0] = self.damage
                dragon_army[self.type][self.name][1] = self.health
                dragon_army[self.type][self.name][2] = self.armor
        else:
            if self.name not in dragon_army[self.type].keys():
                dragon_army[self.type][self.name] = []
                dragon_army[self.type][self.name].append(self.damage)
                dragon_army[self.type][self.name].append(self.health)
                dragon_army[self.type][self.name].append(self.armor)
            else:
                dragon_army[self.type][self.name][0] = self.damage
                dragon_army[self.type][self.name][1] = self.health
                dragon_army[self.type][self.name][2] = self.armor


dragon_army = {}
number_of_dragons = int(input())

# read date form inputs and call add_dragon method from class Dragon
for _ in range(number_of_dragons):
    data = input().split()
    dragon_type = data[0]
    dragon_name = data[1]
    dragon_damage = data[2]
    dragon_health = data[3]
    dragon_armor = data[4]

    if data[2] == 'null':
        dragon_damage = 45
    if data[3] == 'null':
        dragon_health = 250
    if data[4] == 'null':
        dragon_armor = 10

    new_dragon = Dragon(dragon_type, dragon_name, int(dragon_damage), int(dragon_health), int(dragon_armor))
    Dragon.add_dragon(new_dragon)

print(dragon_army)
# {'Red': {'Bazgargal': [100, 2500, 25], 'Obsidion': [220, 2200, 35]}, 'Black': {'Dargonax': [200, 3500, 18]}, 'Blue': {'Kerizsa': [60, 2100, 20], 'Algordox': [65, 1800, 50]}}
# {'Red': {'Bazgargal': [100, 2500, 25], 'Obsidion': [220, 2200, 35]}, 'Black': {'Dargonax': [200, 3500, 18]}, 'Blue': {'Kerizsa': [60, 2100, 20], 'Algordox': [65, 1800, 50]}}
