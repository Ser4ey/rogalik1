import time

import keyboard

import console
import fight
from game_animations import ChooseHero, DrawLevel
import labirint

if __name__ == '__main__':
    # Объект main_console - единственный способ вывода в консоль. Он должен передоваться во все другие объекты
    main_console = console.Console()
    lever_drawer = DrawLevel(main_console)
    player = fight.Player(main_console)


    # Выбор класса персонажа
    hero_class = ChooseHero(main_console).choice_hero()

    main_labirint = labirint.Labyrinth()
    current_level = 1
    while True:
        i = 2
        j = 2

        main_console.restart_work()
        lever_drawer.draw_level_screen(current_level)
        main_console.finish_work()

        main_labirint.generate()
        while not (keyboard.is_pressed('RETURN') and main_labirint.rooms_place[i // 15][j // 36] == 2):
            time.sleep(0.001)
            level, i, j = labirint.move(main_labirint, i, j)
            current_room_number, room_type, used = level.draw(i, j, current_level)

            if current_room_number != -1:
                # print(current_room_number, room_type)

                if room_type == 'с торговцем':
                    if not used:
                        print(f'Торговец не хочет с вами торгавать! Дойдите до 100 уроня!')
                    else:
                        print(f'Я не буду торговать с тобой!!')

                if room_type == 'с фонтаном':
                    if not used:
                        print('Вы востановили 50hp')
                        player.regeneration_health(50)
                    else:
                        print(f'Вы уже пили из фонтана')

                if room_type == 'с сундуком':
                    if not used:
                        print(f'Сундук пуст.')
                    else:
                        print(f'Удивительно, но в сундуке ничего не появилось!')

                time.sleep(3)

            if keyboard.is_pressed('e'):
                main_console.restart_work()
                player.inventory.show_inventory()
                main_console.finish_work()

            print(f'Текущий уровень: {current_level}')
            if (level.rooms[i // 15][j // 36].typeRoom == 3) and (level.rooms[i // 15][j // 36].check == 0):
                print("БОЙ НАЧАЛСЯ!")
                time.sleep(2)
                b = fight.Battle.fight(player, fight.Demon())
                if not b:
                    print(f'Вы погибли!')
                    exit()
                else:
                    print(f'Победа!')
                    time.sleep(2)

                level.rooms[i // 15][j // 36].check = 1

            if (level.rooms[i // 15][j // 36].typeRoom == 4) and (level.rooms[i // 15][j // 36].check == 0):
                print("Воспользуйтесь сундуком, чтобы получить предметы")
            if (level.rooms[i // 15][j // 36].typeRoom == 5) and (level.rooms[i // 15][j // 36].check == 0):
                print("Воспользуйтесь фонтаном, чтобы пополнить здоровье")
            if (level.rooms[i // 15][j // 36].typeRoom == 6) and (level.rooms[i // 15][j // 36].check == 0):
                print("Воспользуйтесь торговцем, чтобы приобрести предметы")
        current_level += 1







