from scenario import *
from qol import *


class Character:
    def __init__(self, name, hp, mp, attack, intelligence, defense, speed, luck):
        self.max_level = 20
        self.max_floor = 50
        self.level_up_experience = 125
        self.unallocated_points = 5
        self.gold = 0
        self.hp_potions = 3
        self.mp_potions = 3

        self.name = name
        self.floor = 49

        self.level = 1
        self.experience = 0
        self.hp = hp
        self.current_hp = hp
        self.mp = mp
        self.current_mp = mp
        self.attack = attack
        self.intelligence = intelligence
        self.defense = defense
        self.speed = speed
        self.luck = luck

    def restore_hp(self):
        if self.hp_potions > 0:
            self.current_hp = self.hp
            print('HP fully restored!')
            self.hp_potions -= 1
        else:
            print('You do not have any HP potions!')

    def restore_mp(self):
        if self.mp_potions > 0:
            self.current_mp = self.mp
            print('MP fully restored!')
            self.mp_potions -= 1
        else:
            print('You do not have any MP potions!')

    def allocate_points(self, stat, points):
        if self.unallocated_points >= points:
            if stat == 'hp':
                setattr(self, stat, getattr(self, stat) + points * 5)
            else:
                setattr(self, stat, getattr(self, stat) + points)
            self.unallocated_points -= points
            print(f'Allocated {points} points to {stat}.')
            return True
        else:
            print('Not enough unallocated points.')
            return False

    def char_creator_menu(self):
        clear()
        draw()
        print(f'{self.__class__.__name__} Base Stats:')
        draw()
        print(f'HP: {self.hp}')
        print(f'MP: {self.mp}')
        print(f'\nATK: {self.attack}')
        print(f'INT: {self.intelligence}')
        print(f'DEF: {self.defense}')
        print(f'SPD: {self.speed}')
        print(f'LUCK: {self.luck}')
        draw()
        print(f'Unallocated Points: {self.unallocated_points}')
        draw()

    def game_menu(self):
        clear()
        draw()
        print('CHARACTER INFO')
        draw()
        print(f'{self.name}')
        print(f'LVL {self.level} {self.__class__.__name__}')
        print(f'Exp: {self.experience}/{self.level_up_experience}')
        draw()
        print('STATUS')
        draw()
        print(f'HP: {self.current_hp}/{self.hp}')
        print(f'MP: {self.current_mp}/{self.mp}')
        print(f'Gold: {self.gold}')
        draw()
        print('STATS')
        draw()
        print(f'ATK: {self.attack}')
        print(f'INT: {self.intelligence}')
        print(f'DEF: {self.defense}')
        print(f'SPD: {self.speed}')
        print(f'LUCK: {self.luck}')
        draw()
        print(f'Unallocated Points: {self.unallocated_points}')

    def gain_experience(self, experience):
        self.experience += experience
        if self.experience >= self.level_up_experience:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= self.level_up_experience
        self.level_up_experience = round(self.level_up_experience * 1.2)
        draw()
        print(f'You have leveled up to Level {self.level}.')
        self.unallocated_points += 2
        self.hp += 10
        self.mp += 5
        self.attack += random.randint(0, 1)
        self.intelligence += random.randint(0, 1)
        self.defense += random.randint(0, 1)
        self.speed += random.randint(0, 1)
        self.luck += random.randint(0, 1)

    def __str__(self):
        return f'Class: {self.__class__.__name__}\n\nHP: {self.hp}\nATK: {self.attack}\nINT: {self.intelligence}\nDEF: {self.defense}\nSPD: {self.speed}\nLUCK: {self.luck}\n\nUnallocated Points: {self.unallocated_points}'

    def calculate_crit(self):
        crit_strike = 5 + (self.luck * .5)
        calculate = random.randint(1, 100)
        if calculate <= crit_strike:
            return True
        else:
            return False

    def basic_attack(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        if self.attack >= enemy.defense:
            damage = self.attack * 2 - enemy.defense
        else:
            damage = self.attack * self.attack // enemy.defense
        if crit:
            damage *= 2
        if damage > 0:
            enemy.current_hp -= damage
            print(f'{self.name} hits {enemy.name} for {damage} damage!')
            if crit:
                print('Critical Hit!')

    def use_ability(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        if self.current_mp > 0:
            damage = random.randint(10, 20)
            if crit:
                damage *= 2
            enemy.current_hp -= damage
            self.current_mp -= 10
            print(f'{self.name} uses a spell and deals {damage} damage to {enemy.name}!')
            if crit:
                print('Critical Hit!')
        else:
            print(f'{self.name} does not have enough MP to use a spell!')

    def scenario(self):
        num = random.randint(1, 275)
        num += (self.luck // 2)
        if 250 <= num:
            scenario_good(self)
        elif 50 <= num <= 249:
            scenario_neutral(self)
        elif 0 <= num <= 49:
            scenario_bad(self)


class Knight(Character):
    def __init__(self):
        super().__init__(name='', hp=150, mp=60, attack=6, intelligence=4, defense=8, speed=5, luck=5)

    def basic_attack(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        if self.attack >= enemy.defense:
            damage = self.attack * 2 - enemy.defense
        else:
            damage = self.attack * self.attack // enemy.defense
        if crit:
            damage *= 2
        if damage > 0:
            enemy.current_hp -= damage
            print(f'{self.name} strikes {enemy.name} for {damage} damage!')
            if crit:
                print('Critical Hit!')

    def use_ability(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        if self.current_mp >= 15:
            if self.attack >= enemy.defense:
                damage = self.attack * 2 - enemy.defense
            else:
                damage = self.attack * self.attack // enemy.defense
            damage *= 2
            if crit:
                damage *= 2
            enemy.current_hp -= damage
            self.current_mp -= 15
            print(f'{self.name} uses Shield Bash and deals {damage} damage to {enemy.name}!')
            if crit:
                print('Critical Hit!')
        else:
            print(f'{self.name} does not have enough MP to use Shield Bash!')


class Ranger(Character):
    def __init__(self):
        super().__init__(name='', hp=120, mp=80, attack=7, intelligence=5, defense=5, speed=7, luck=6)

    def basic_attack(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        if self.attack >= enemy.defense:
            damage = self.attack * 2 - enemy.defense
        else:
            damage = self.attack * self.attack // enemy.defense
        if crit:
            damage *= 2
        if damage > 0:
            enemy.current_hp -= damage
            print(f'{self.name} shoots {enemy.name} for {damage} damage!')
            if crit:
                print('Critical Hit!')

    def use_ability(self, enemy):
        if self.current_mp >= 20:
            self.current_mp -= 20
            times_hit = random.randint(2, 4)
            for num in range(times_hit):
                crit = False
                if self.calculate_crit():
                    crit = True
                damage = random.randint(self.attack, self.attack * 2)
                if crit:
                    damage *= 2
                damage -= enemy.defense
                if damage <= 0:
                    damage = 1
                enemy.current_hp -= damage
                print(f'{self.name} uses Multi-Shot and deals {damage} damage to {enemy.name}!')
                if crit:
                    print('Critical Hit!')
        else:
            print(f'{self.name} does not have enough MP to use Multi-Shot!')


class Wizard(Character):
    def __init__(self):
        super().__init__(name='', hp=120, mp=120, attack=5, intelligence=9, defense=5, speed=5, luck=7)

    def basic_attack(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        if (self.attack // 2) + (self.intelligence // 2) >= enemy.defense:
            damage = (self.attack // 2) + (self.intelligence // 2) * 2 - enemy.defense
        else:
            damage = ((self.attack // 2) + (self.intelligence // 2) * (self.attack // 2) + (
                    self.intelligence // 2)) // enemy.defense
        if crit:
            damage *= 2
        if damage > 0:
            enemy.current_hp -= damage
            print(f'{self.name} zaps {enemy.name} for {damage} damage!')
            if crit:
                print('Critical Hit!')

    def use_ability(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True
        if self.current_mp > 30:
            damage = self.intelligence * 2
            if crit:
                damage *= 2
            damage -= (enemy.defense // 2)
            enemy.current_hp -= damage
            self.current_mp -= 30
            print(f'{self.name} casts Fireball and deals {damage} damage to {enemy.name}!')
            if crit:
                print('Critical Hit!')
        else:
            print(f'{self.name} does not have enough MP to cast Fireball!')


class Rogue(Character):
    def __init__(self):
        super().__init__(name='', hp=110, mp=60, attack=6, intelligence=5, defense=5, speed=8, luck=8)

    def calculate_crit(self):
        crit_strike = 25 + (self.luck * .5)
        calculate = random.randint(1, 100)
        if calculate <= crit_strike:
            return True
        else:
            return False

    def basic_attack(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        if self.attack >= enemy.defense:
            damage = self.attack * 2 - enemy.defense
        else:
            damage = self.attack * self.attack // enemy.defense
        if crit:
            damage *= 2
        if damage > 0:
            enemy.current_hp -= damage
            print(f'{self.name} stabs {enemy.name} for {damage} damage!')
            if crit:
                print('Critical Hit!')

    def use_ability(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True
        if self.current_mp > 15:
            damage = random.randint(self.attack + self.attack, self.attack + (self.attack * 2))
            if crit:
                damage *= 2
            bonus = random.randint(1, self.luck)
            damage += bonus
            damage -= (enemy.defense // 2)
            enemy.current_hp -= damage
            self.current_mp -= 15
            print(f'{self.name} Back Stabs {enemy.name} and does {damage} damage!')
            if crit:
                print('Critical Hit!')
        else:
            print(f'{self.name} does not have enough MP to use Back Stab!')


def char_creator():
    classes = {
        'knight': Knight,
        'ranger': Ranger,
        'wizard': Wizard,
        'rogue': Rogue
    }
    while True:
        clear()
        draw()
        print('Choose a Class:')
        draw()
        for cls_name in classes:
            print(f'- {cls_name.capitalize()}')
        draw()
        cls_choice = input('> ')
        if cls_choice.lower().strip() in classes:
            break
        else:
            continue

    player = classes[cls_choice.lower().strip()]()

    stats = ('attack', 'intelligence', 'defense', 'speed', 'luck')

    while player.unallocated_points > 0:
        player.char_creator_menu()
        stat = input('Which stat would you like to allocate points to? (ATTACK/INTELLIGENCE/DEFENSE/SPEED/LUCK) ')
        if stat.lower().strip() in stats:
            while True:
                try:
                    while True:
                        points = int(input('How many points would you like to allocate? '))
                        if player.allocate_points(stat.lower().strip(), points):
                            break
                        else:
                            draw()
                            continue
                except ValueError:
                    continue
                break
        else:
            pass
    while True:
        player.char_creator_menu()
        name = input('What is your name? ')
        player.name = name
        if name == '':
            continue
        else:
            break

    draw()
    print('Character creation complete!')
    draw()
    input('Press enter to begin game...')
    player.current_hp = player.hp
    return player


if __name__ == '__main__':
    pass
