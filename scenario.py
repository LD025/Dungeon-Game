import random
from qol import *


def scenario_good(self):
    library(self)


def scenario_neutral(self):
    roll = random.randint(1, 2)
    if roll == 1:
        fountain_of_healing(self)
    elif roll == 2:
        treasure_chest(self)


def scenario_bad(self):
    trap(self)


def library(self):
    print('You wander into a large library, there seems to be no one here.')
    print('A magical aura envelops the room...')
    print('You are filled with knowledge!')
    self.level_up()
    self.experience = 0
    draw()
    input('Press enter to continue...')


def fountain_of_healing(self):
    print('While examining the room, you come across a bright, luminescent fountain...')
    print('You are strangely drawn to it. Touch the fountain? (Yes/No)')
    draw()
    while True:
        choice = input('> ')
        if choice.lower().strip() == 'yes':
            chance = random.randint(1, 10)
            if chance > 7:
                self.current_hp = self.hp
                self.current_mp = self.mp
                draw()
                print('You touch the fountain, activating its restorative powers.')
                print('Your HP and MP have been fully restored!')
                draw()
                break
            else:
                draw()
                print('You touch the fountain curiously.')
                print('Nothing happened.')
                draw()
                break
        elif choice.lower().strip() == 'no':
            draw()
            print('You decide to ignore your urge to touch the fountain.')
            print('Perhaps you made the right choice.')
            draw()
            break
    input('Press enter to continue...')


def treasure_chest(self):
    print('As you examine the room, you come across a chest...')
    print('Open the chest? (Yes/No)')
    draw()
    while True:
        choice = input('> ')
        if choice.lower().strip() == 'yes':
            loot_chance = random.randint(1, 6)
            if loot_chance > 4:
                draw()
                gold = random.randint(10, (25 + self.floor))
                self.gold += gold
                print('You open the chest, it is full of gold!')
                print(f'You have gained {gold} gold.')
                draw()
                break
            else:
                draw()
                print('You open the chest. It is empty.')
                print('It appears to have already been looted.')
                draw()
                break
        elif choice.lower().strip() == 'no':
            draw()
            print('You decide to not open the chest')
            print('There could have been something dangerous inside.')
            draw()
            break
    input('Press enter to continue...')


def trap(self):
    print('As you explore the room, you are not mindful enough of your surroundings.')
    print('You step on a trap!')
    damage = random.randint(5, 15)
    self.current_hp -= damage
    draw()
    print(f'You take {damage} damage.')
    draw()
    input('Press enter to continue...')


if __name__ == '__main__':
    pass
