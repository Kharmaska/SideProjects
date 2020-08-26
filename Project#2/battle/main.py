from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 8, "dmg": 50},
         {"name": "Blizzard", "cost": 20, "dmg": 90},]

player = Person(460, 65, 68, 34, magic)

enemy = Person(1200, 65, 45, 25, magic)

running = True

while running:
    print("Lets overflow this stack.")