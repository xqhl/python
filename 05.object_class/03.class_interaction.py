# interaction
# 对打的游戏

import random

class Character:
    def __init__(self, boole, g, f):
        self.boole = boole
        self.g = g
        self.f = f
        self.buffer = random.randint(0, 9)

    def attack(self, character):
        character.boole -= self.g + self.buffer


r01 = Character(100, 5, 3)
r02 = Character(100, 5, 5)

for i in range(15):
    if i % 2 == 0:
        r01.attack(r02)
    else:
        r02.attack(r01)
else:
    print("r01's boole: {}".format(r01.boole))
    print("r02's boole: {}".format(r02.boole))
