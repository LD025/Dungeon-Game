import pickle
import random
from text import *
from qol import *
from character_info import char_creator
from enemy_info import generate_enemy
from battle import battle

game_name = 'Dungeon Game'


def check_for_death(player):
    if player.current_hp <= 0:
        return True
    else:
        return False


def show_map(x, y):
    funct_map = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]

    for i in range(len(funct_map)):
        if y == i:
            y_location = i
        for j in range(len(funct_map[0])):
            if x == j:
                x_location = j

    funct_map[y_location][x_location] = 1

    for funct_row in funct_map:
        print(funct_row)


def generate_map(x, y):
    funct_map = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]

    rooms = {'battle': 6, 'empty': 8, 'scenario': 5, 'shop': 2, 'ladder': 3, 'entrance': 1}

    for i in range(len(funct_map)):
        for j in range(len(funct_map[0])):
            while True:
                if i == y and j == x:
                    funct_map[i][j] = 'entrance'
                    rooms['entrance'] -= 1
                    break
                room = random.randint(1, 5)
                if room == 1:
                    if rooms['battle'] == 0:
                        continue
                    else:
                        funct_map[i][j] = 'battle'
                        rooms['battle'] -= 1
                        break
                elif room == 2:
                    if rooms['empty'] == 0:
                        continue
                    else:
                        funct_map[i][j] = 'empty'
                        rooms['empty'] -= 1
                        break
                elif room == 3:
                    if rooms['scenario'] == 0:
                        continue
                    else:
                        funct_map[i][j] = 'scenario'
                        rooms['scenario'] -= 1
                        break
                elif room == 4:
                    if rooms['shop'] == 0:
                        continue
                    else:
                        funct_map[i][j] = 'shop'
                        rooms['shop'] -= 1
                        break
                elif room == 5:
                    if rooms['ladder'] == 0:
                        continue
                    else:
                        funct_map[i][j] = 'ladder'
                        rooms['ladder'] -= 1
                        break

    return funct_map


def check_area(floor):
    if floor <= 10:
        return 'CATACOMBS'
    elif 10 < floor <= 20:
        return 'ABYSSAL TUNNELS'
    elif 20 < floor <= 30:
        return 'CURSED CRYPTS'
    elif 30 < floor <= 40:
        return 'GLOOMHAVEN ASYLUM'
    elif 40 < floor <= 50:
        return 'CORRIDOR OF BONES'


def check_room(play_map, x, y):
    room = play_map[y][x]
    return room


def save(player, map):
    with open('save.pickle', 'wb') as file:
        pickle.dump(player, file)
    with open('map.pickle', 'wb') as file:
        pickle.dump(map, file)
    draw()
    print('Game Saved.')
    draw()
    input('Press enter to continue...')


if __name__ == "__main__":
    stats = ('attack', 'intelligence', 'defense', 'speed', 'luck')
    run = True
    menu = True
    play = False
    about = False

    while run:
        while menu:
            clear()
            draw()
            print(f'Welcome to {game_name}!')
            draw()
            print('New Game - 1')
            print('Load Game - 2')
            print('About - 3')
            print('Quit - 4')
            draw()

            choice = input('> ')

            if choice == '1':
                new_game = True
                while new_game:
                    clear()
                    draw()
                    print('NEW GAME')
                    draw()
                    new_game_choice = input('Start a new game? (Yes/No) ')
                    if new_game_choice.lower().strip() == 'yes':
                        new_game = False
                        char = char_creator()
                        x_pos = 2
                        y_pos = 4
                        current_room = 'entrance'
                        player_map = generate_map(x_pos, y_pos)
                        play = True
                    elif new_game_choice.lower().strip() == 'no':
                        new_game = False
            elif choice == '2':
                load_game = True
                while load_game:
                    try:
                        with open('save.pickle', 'rb') as file:
                            char = pickle.load(file)
                        clear()
                        draw()
                        print('LOAD GAME')
                        draw()
                        print(f'{char.name}')
                        print(f'LVL {char.level} {char.__class__.__name__}')
                        print(f'Floor {char.floor}')
                        draw()
                        load = input('Continue this save? (Yes/No) ')
                        if load.lower().strip() == 'yes':
                            with open('map.pickle', 'rb') as file:
                                x_pos, y_pos, current_room, player_map = pickle.load(file)
                            play = True
                            load_game = False
                        elif load.lower().strip() == 'no':
                            load_game = False
                    except FileNotFoundError:
                        clear()
                        draw()
                        print('No save found.')
                        draw()
                        input('Press enter to return to main menu...')
                        load_game = False
            elif choice == '3':
                clear()
                draw()
                print(f'What is {game_name}?')
                draw()
                game_description(game_name)
                draw()
                input('Press enter to return to main menu...')
            elif choice == '4':
                quit()

            while play:
                examine = False
                move = False
                use_item = False

                if char.floor > char.max_floor:
                    clear()
                    draw()
                    print('CONGRATULATIONS!')
                    draw()
                    print('You have escaped the dungeon.')
                    draw()
                    input('Press enter to start a new game!')
                    play = False
                    break

                if check_for_death(char):
                    clear()
                    draw()
                    print('GAME OVER')
                    draw()
                    print('You have died...')
                    print(f'You made it to Floor {char.floor}.')
                    draw()
                    input('Press enter to start a new game!')
                    play = False
                    break

                current_area = check_area(char.floor)
                current_room = check_room(player_map, x_pos, y_pos)
                map_info = [x_pos, y_pos, current_room, player_map]
                x_length = len(player_map[0]) - 1
                y_length = len(player_map) - 1

                clear()
                draw()
                print(f'FLOOR {char.floor} - {current_area}')
                draw()
                show_map(x_pos, y_pos)
                # for row in player_map:
                #     print(row)
                draw()
                print(f'HP: {char.current_hp}/{char.hp} \nMP: {char.current_mp}/{char.mp}')
                draw()
                print('Check Room - 1')
                print('Move - 2')
                print('Items - 3')
                print('Character - 4')
                print('Save Game - 5')
                print('Quit - 6')
                draw()

                play_choice = input('> ')

                if play_choice == '1':
                    examine = True
                if play_choice == '2':
                    move = True
                if play_choice == '3':
                    use_item = True
                if play_choice == '4':
                    # TODO: clean up
                    end_early = False
                    char.game_menu()
                    while char.unallocated_points > 0:
                        while True:
                            draw()
                            print(f'You have {char.unallocated_points} Unallocated Stat points.')
                            print('Would you like to spend them? (Yes/No) ')
                            draw()
                            choice_allocate = input('> ')
                            if choice_allocate.lower().strip() == 'yes':
                                while True:
                                    draw()
                                    stat = input(
                                        'Which stat would you like to allocate points to? (ATTACK/INTELLIGENCE/DEFENSE/SPEED/LUCK) ')
                                    if stat.lower().strip() in stats:
                                        while True:
                                            try:
                                                while True:
                                                    points = int(input('How many points would you like to allocate? '))
                                                    if char.allocate_points(stat.lower().strip(), points):
                                                        clear()
                                                        char.game_menu()
                                                        break
                                                    else:
                                                        draw()
                                                        continue
                                            except ValueError:
                                                continue
                                            break
                                        break
                                    else:
                                        continue
                                break
                            elif choice_allocate.lower().strip() == 'no':
                                end_early = True
                                break
                            else:
                                print('Invalid Input.')
                                end_early = True
                                break
                        if end_early:
                            break
                        else:
                            continue
                    draw()
                    input('Press enter to exit stat menu...')
                if play_choice == '5':
                    clear()
                    save(char, map_info)
                    play_choice = ''
                if play_choice == '6':
                    play = False

                while examine:
                    # for row in player_map:
                    #     print(row)
                    # print(f'Current Floor: {char.floor}')
                    # print(f'Current room: {current_room}')
                    # print(f'You are currently in {player_map[y_pos][x_pos]}.')
                    clear()
                    draw()
                    print('You examine the room.')
                    draw()
                    if current_room == 'empty':
                        print('The room is empty.')
                        draw()
                        input('Press enter to continue...')
                    elif current_room == 'ladder':
                        print('You find a ladder that leads to the next floor.')
                        print('Take it? (Yes/No)')
                        draw()
                        while True:
                            ladder_choice = input('> ')
                            if ladder_choice.lower().strip() == 'yes':
                                player_map = generate_map(x_pos, y_pos)
                                char.floor += 1
                                break
                            elif ladder_choice.lower().strip() == 'no':
                                break
                    elif current_room == 'scenario':
                        char.scenario()
                        player_map[y_pos][x_pos] = 'empty'
                    elif current_room == 'battle':
                        print('You can feel something sneak up behind you..')
                        draw()
                        input('Press enter to continue...')
                        clear()
                        enemy = generate_enemy(char.floor)
                        battle(char, enemy)
                        player_map[y_pos][x_pos] = 'empty'
                    elif current_room == 'entrance':
                        print('You are in the entrance.')
                        draw()
                        input('Press enter to continue...')
                    elif current_room == 'shop':
                        shop_hp = False
                        shop_mp = False
                        print('While exploring the room, you encounter a friendly skeleton.')
                        shop_item = random.randint(1, 5)
                        shop_price = random.randint(5, 25) + random.randint(1, ((2 + char.gold) // 2))
                        if shop_item > 2:
                            shop_hp = True
                            print(f'He offers to sell you an HP Potion for {shop_price} gold.')
                        else:
                            shop_mp = True
                            print(f'He offers to sell you an MP Potion for {shop_price} gold.')
                        draw()
                        print('Accept his offer? (Yes/No)')
                        draw()
                        while True:
                            shop_choice = input('> ')
                            if shop_choice.lower().strip() == 'yes':
                                if char.gold >= shop_price:
                                    if shop_hp:
                                        char.hp_potions += 1
                                        char.gold -= shop_price
                                        draw()
                                        print('You buy the HP Potion from the skeleton.')
                                        print('He bids you farewell and wanders away.')
                                        shop_hp = False
                                        break
                                    elif shop_mp:
                                        char.mp_potions += 1
                                        char.gold -= shop_price
                                        draw()
                                        print('You buy the MP Potion from the skeleton.')
                                        print('He bids you farewell and wanders away.')
                                        shop_mp = False
                                        break
                                else:
                                    draw()
                                    print('The skeleton realizes you do not have enough gold.')
                                    print('He calls you broke and wanders away.')
                                    break
                            elif shop_choice.lower().strip() == 'no':
                                draw()
                                print('You decline the offer. The skeleton bids you farewell and wanders away.')
                                break
                        draw()
                        input('Press enter to continue...')
                        player_map[y_pos][x_pos] = 'empty'
                    examine = False
                while move:
                    clear()
                    draw()
                    print('Move where?')
                    draw()
                    print('Press W to move up')
                    print('Press A to move left')
                    print('Press S to move down')
                    print('Press D to move right')
                    draw()
                    while True:
                        move_choice = input('> ')

                        if move_choice.lower().strip() == 'w':
                            if y_pos == 0:
                                draw()
                                print('You cannot move up any further!')
                                draw()
                            else:
                                y_pos -= 1
                                move = False
                                break
                        if move_choice.lower().strip() == 'a':
                            if x_pos == 0:
                                draw()
                                print('You cannot move left any further!')
                                draw()
                            else:
                                x_pos -= 1
                                move = False
                                break
                        if move_choice.lower().strip() == 's':
                            if y_pos == y_length:
                                draw()
                                print('You cannot move down any further!')
                                draw()
                            else:
                                y_pos += 1
                                move = False
                                break
                        if move_choice.lower().strip() == 'd':
                            if x_pos == x_length:
                                draw()
                                print('You cannot move right any further!')
                                draw()
                            else:
                                x_pos += 1
                                move = False
                                break

                while use_item:
                    clear()
                    draw()
                    print('INVENTORY')
                    draw()
                    print(f'HP Potions: {char.hp_potions}')
                    print(f'MP Potions: {char.mp_potions}')
                    draw()
                    print('Press 1 to consume HP Potion.')
                    print('Press 2 to consume MP Potion.')
                    print('Press 3 to exit.')
                    draw()
                    while True:
                        item_choice = input('> ')
                        if item_choice == '1':
                            draw()
                            char.restore_hp()
                            draw()
                            input('Press enter to return to menu...')
                            use_item = False
                            break
                        elif item_choice == '2':
                            draw()
                            char.restore_mp()
                            draw()
                            input('Press enter to return to menu...')
                            use_item = False
                            break
                        elif item_choice == '3':
                            use_item = False
                            break
