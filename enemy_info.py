import random


class Enemy:
    def __init__(self, name, hp, mp, attack, intelligence, defense, speed, luck, xp_yield, gold_yield):
        self.name = name
        self.hp = hp
        self.current_hp = hp
        self.mp = mp
        self.current_mp = mp
        self.attack = attack
        self.intelligence = intelligence
        self.defense = defense
        self.speed = speed
        self.luck = luck
        self.xp_yield = xp_yield
        self.gold_yield = gold_yield

    def __str__(self):
        return f'{self.name}\nATK: {self.attack}\nINT: {self.intelligence}\nDEF: {self.defense}\nSPD: {self.speed}\nLUCK: {self.luck}'

    def battle_ai(self, enemy):
        roll = random.randint(1, 10)
        if roll == 1 or roll == 10:
            self.use_ability(enemy)
        else:
            self.basic_attack(enemy)

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

        damage = random.randint(10, 20)
        if crit:
            damage *= 2
        enemy.current_hp -= damage
        print(f'{self.name} uses their ability and deals {damage} damage to {enemy.name}!')
        if crit:
            print('Critical Hit!')


class Zombie(Enemy):
    def use_ability(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        damage = random.randint(10, 20)
        if crit:
            damage *= 2
        enemy.current_hp -= damage
        print(f'{self.name} uses Bite and deals {damage} damage to {enemy.name}!')
        if crit:
            print('Critical Hit!')


class Skeleton(Enemy):
    def use_ability(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        damage = random.randint(10, 20)
        if crit:
            damage *= 2
        enemy.current_hp -= damage
        print(f'{self.name} uses Bone Throw and deals {damage} damage to {enemy.name}!')
        if crit:
            print('Critical Hit!')


class Spider(Enemy):
    def use_ability(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        damage = random.randint(10, 20)
        if crit:
            damage *= 2
        enemy.current_hp -= damage
        print(f'{self.name} uses Venomous Bite and deals {damage} damage to {enemy.name}!')
        if crit:
            print('Critical Hit!')


class Slime(Enemy):
    def use_ability(self, enemy):
        crit = False
        if self.calculate_crit():
            crit = True

        damage = random.randint(10, 20)
        if crit:
            damage *= 2
        enemy.current_hp -= damage
        print(f'{self.name} uses Jump and deals {damage} damage to {enemy.name}!')
        if crit:
            print('Critical Hit!')


def generate_enemy(floor_level):
    hp = random.randint(10, 20) + 5 * floor_level
    mp = random.randint(5, 10) + 2 * floor_level
    attack = random.randint(3, 6) + random.randint(1, floor_level)
    intelligence = random.randint(3, 6) + random.randint(1, floor_level)
    defense = random.randint(2, 5) + random.randint(1, floor_level)
    speed = random.randint(3, 6) + random.randint(1, floor_level)
    luck = random.randint(1, 3) + random.randint(1, floor_level)
    xp_yield = attack + intelligence + defense + speed + luck
    gold_yield = random.randint(xp_yield//2, xp_yield) // 2

    enemy_type = random.randint(1, 4)
    if enemy_type == 1:
        return Zombie('Zombie', hp, mp, attack, intelligence, defense, speed, luck, xp_yield, gold_yield)
    if enemy_type == 2:
        return Skeleton('Skeleton', hp, mp, attack, intelligence, defense, speed, luck, xp_yield, gold_yield)
    if enemy_type == 3:
        return Spider('Spider', hp, mp, attack, intelligence, defense, speed, luck, xp_yield, gold_yield)
    if enemy_type == 4:
        return Slime('Slime', hp, mp, attack, intelligence, defense, speed, luck, xp_yield, gold_yield)


if __name__ == '__main__':
    pass
