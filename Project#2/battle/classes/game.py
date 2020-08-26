import random



class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    B0LD = "\033[1m"
    UNDERLINE = "\033[4m"

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_dmg(self, index):
        mgl = self.magic[index]["dmg"] - 5
        mgh = self.magic[index]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, index):
        return self.magic[index]["name"]

    def get_spell_mp_cost(self, index):
        return self.magic[index]["cost"]

    def choose_action(self):
        index = 1
        print("Actions")
        for item in self.actions:
            print(str(index) + ":", item)
            index += 1

    def choose_magic(self):
        index = 1
        print("Magic")
        for spell in self.magic:
            print("        " + str(index) + ':', spell.name, '(cost: ', str(spell.cost) + ')')
            index += 1
            