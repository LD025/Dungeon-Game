import random
from qol import *


def enemy_info(enemy):
    draw()
    print('ENEMY INFORMATION')
    draw()
    print(enemy)
    draw()


def battle(player, enemy):

    draw()
    print(f'{enemy.name} Attacks!')

    while player.current_hp > 0 and enemy.current_hp > 0:
        draw()
        print(f'{player.name}: HP {player.current_hp}/{player.hp}, MP {player.current_mp}/{player.mp}')
        print(f'{enemy.name}: HP {enemy.current_hp}/{enemy.hp}')
        draw()
        print('1 - Attack')
        print('2 - Use Ability')
        print('3 - Enemy Info')
        print('4 - Use Item')
        print('5 - Run')
        draw()
        choice = input(f'> {player.name}, chose your action: ')

        if choice == '1':
            clear()
            draw()
            player.basic_attack(enemy)
            if enemy.current_hp > 0:
                draw()
                enemy.battle_ai(player)
        elif choice == '2':
            clear()
            draw()
            player.use_ability(enemy)
            if enemy.current_hp > 0:
                draw()
                enemy.battle_ai(player)
        elif choice == '3':
            clear()
            enemy_info(enemy)
            if enemy.current_hp > 0:
                enemy.battle_ai(player)
        elif choice == '4':
            clear()
            draw()
            print('INVENTORY')
            draw()
            print(f'HP Potions: {player.hp_potions}')
            print(f'MP Potions: {player.mp_potions}')
            draw()
            while True:
                print('Press 1 to consume HP Potion.')
                print('Press 2 to consume MP Potion.')
                print('Press 3 to exit.')
                draw()
                item_choice = input('> ')
                if item_choice == '1':
                    clear()
                    draw()
                    player.restore_hp()
                    if enemy.current_hp > 0:
                        draw()
                        enemy.battle_ai(player)
                    break
                elif item_choice == '2':
                    clear()
                    draw()
                    player.restore_mp()
                    if enemy.current_hp > 0:
                        draw()
                        enemy.battle_ai(player)
                    break
                elif item_choice == '3':
                    clear()
                    break
        elif choice == '5':
            if player.speed > enemy.speed:
                run_chance = random.randint(1, 10)
                if run_chance > 1:
                    break
                else:
                    clear()
                    draw()
                    print('Cannot escape!')
                    if enemy.current_hp > 0:
                        draw()
                        enemy.battle_ai(player)
            if player.speed == enemy.speed:
                run_chance = random.randint(1, 10)
                if run_chance > 4:
                    break
                else:
                    clear()
                    draw()
                    print('Cannot escape!')
                    if enemy.current_hp > 0:
                        draw()
                        enemy.battle_ai(player)
            if player.speed < enemy.speed:
                run_chance = random.randint(1, 10)
                if run_chance > 6:
                    break
                else:
                    clear()
                    draw()
                    print('Cannot escape!')
                    if enemy.current_hp > 0:
                        draw()
                        enemy.battle_ai(player)

    if player.current_hp > 0 >= enemy.current_hp:
        draw()
        print(f'{player.name} has defeated {enemy.name}!')
        player.gold += enemy.gold_yield
        print(f'You have gained {enemy.xp_yield} experience and {enemy.gold_yield} gold.')
        player.gain_experience(enemy.xp_yield)
        draw()
        input('Press enter to continue...')
    elif player.current_hp <= 0 < enemy.current_hp:
        draw()
        print(f'{player.name} has been defeated!')
        draw()
        input('Press enter to continue...')
    elif player.current_hp > 0 and enemy.current_hp > 0:
        clear()
        draw()
        print(f'{player.name} has fled from battle!')
        draw()
        input('Press enter to continue...')


if __name__ == '__main__':
    pass
