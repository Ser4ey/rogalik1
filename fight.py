import random
from typing import List
from enum import Enum
from items import *
from console import Console


class Unit:
    def __init__(self) -> None:
        self.max_health = 100
        self.current_health = self.max_health

        self.base_attack = 10
        self.real_attack = self.base_attack

        self.base_armor = 10
        self.real_armor = self.base_armor

        # self.agility = 10

        self.estus = 3  # TODO: ??? 인벤토리로 이동 ???
        self.current_weapon = None
        self.current_armor = None

    # Конечная функция, которая наносит урон
    def get_damage(self, attack) -> None:
        self.current_health -= attack * self.multiplier()

    def get_real_attack(self):
        if self.current_weapon:
            return self.base_attack + self.current_weapon.item_damage
        else:
            return self.base_attack

    # Функция, которая возвращает множитель, чтобы уменьшить урон, в зависимости от количества брони
    def multiplier(self):
        full_armor = self.get_total_armor()
        damage_multiplier = 1 - ((0.06 * full_armor) / (1 + 0.06 * abs(full_armor)))
        return damage_multiplier

    def get_total_armor(self):
        if self.current_armor:
            return self.base_armor + self.current_armor.item_armor
        else:
            return self.base_armor


class Player(Unit):
    def __init__(self, console: Console) -> None:
        super().__init__()
        self.level = 1
        self.money = 0
        self.exp_for_level = 10
        self.current_exp = 0

        self.armor_by_item = 0
        self.attack_by_item = 0

        # self.effects: List[Effect] = []
        self.inventory = Inventory(console, self)


    def level_up(self, experience) -> None:
        self.current_exp += experience
        if self.current_exp >= self.exp_for_level:
            # Если опыта набралось нужное кол-во для поднятия уровня, то поднимаем уровень и кол-во exp для нового уровня
            self.current_exp = self.current_exp - self.exp_for_level
            self.level += 1
            self.exp_for_level = self.level * 10

    def equip_armor(self, new_armor: Armor):
        self.current_armor = new_armor
        self.real_armor = self.base_armor + new_armor.item_armor

    def unequip_armor(self):
        if self.current_armor is None:
            return
        self.real_armor -= self.current_armor.item_armor
        self.current_armor = None

    def equip_weapon(self, new_weapon: Weapon):
        self.current_weapon = new_weapon
        self.real_attack = self.base_attack + new_weapon.item_damage

    def unequip_weapon(self):
        if self.current_weapon is None:
            return
        self.real_attack -= self.current_weapon.item_damage
        self.current_weapon = None

    def regeneration_health(self, regeneration_value):
        difference_in_health = self.max_health - self.current_health
        if difference_in_health >= regeneration_value and self.estus > 0:
            self.current_health += regeneration_value
            self.estus -= 1
        elif difference_in_health < regeneration_value and self.estus > 0:
            self.current_health += difference_in_health
            self.estus -= 1


class Inventory:
    def __init__(self, console: Console, player: Player):
        self.items = []
        self.console = console
        self.player = player

    def add_item(self, item: Item):
        self.items.append(item)

    def del_item_by_index(self, index: int):
        try:
            self.items.pop(index)
            return True
        except:
            return False

    def draw_items(self, current_item: int):
        start_x = 3
        start_y = 8
        if len(self.items) == 0:
            self.console.write_line(start_x, start_y, f'У вас ничего нет!')
            return

        for i in range(len(self.items)):
            item_type = start_x, start_y, type(self.items[i]).__name__

            if current_item == i:
                line_to_write = f'[*] '
            else:
                line_to_write = f'[ ] '

            line_to_write += f'Название предмета: {self.items[i]} Тип предмета: {item_type} '
            if self.items[i] == self.player.current_armor or self.items[i] == self.player.current_weapon:
                line_to_write += '(экипировано)'
            start_y += 2

    def show_inventory(self):
        self.console.clear()
        self.console.write_border(0, 0, 150, 49)
        self.console.write_line(3, 2, f'Текущий уровень: {self.player.level}')
        self.console.write_line(3, 3, f'Опыта: {self.player.current_exp}/{self.player.exp_for_level}')
        self.console.write_line(3, 4, f'Баланс: {self.player.money}')
        self.console.write_line(3, 5, f'Здроье: {self.player.current_health}/{self.player.max_health}')

        self.console.write_line(3, 7, 'Инвентарь:')

        self.draw_items(0)
        char = self.console.get_char()


class Enemy(Unit):
    money_after_death = 10
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.money = 10


class Knight(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.exp_after_death = 20
        self.exp_after_death = 15
        # self.agility = self.agility * 1.5
        self.armor = self.base_armor * 1.5
        self.max_health = self.max_health * 0.7

    knight_ascii = r'''
                   _.--.    .--._
                 ."  ."      ".  ".
                ;  ."    /\    ".  ;
                ;  '._,-/  \-,_.`  ;
                \  ,`  / /\ \  `,  /
                 \/    \/  \/    \/
                 ,=_    \/\/    _=,
                 |  "_   \/   _"  |
                 |_   '"-..-"'   _|
                 | "-.        .-" |
                 |    "\    /"    |
                 |      |  |      |
         ___     |      |  |      |     ___
     _,-",  ",   '_     |  |     _'   ,"  ,"-,_
   _(  \  \   \"=--"-.  |  |  .-"--="/   /  /  )_
 ."  \  \  \   \      "-'--'-"      /   /  /  /  ".
|     \  \  \   \                  /   /  /  /     |
|      \  \  \   \                /   /  /  /      |
'''


class Skeleton(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.exp_after_death = 15
        self.max_health = self.max_health * 1.3
        # self.agility = self.agility * 0.4
        self.attack = self.real_attack * 0.4

    skeleton_ascii = r'''
                              _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      )\
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  \
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. \
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
    '''

class Demon(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.exp_after_death = 15
        self.attack = self.real_attack * 1.3
        self.armor = self.base_armor * 0.7

    demon_ascii = r'''
 *                       *
    *                 *
   )       (\___/)     (
* /(       \ (. .)     )\ *
  # )      c\   >'    ( #
   '         )-_/      '
 \\|,    ____| |__    ,|//
   \ )  (  `  ~   )  ( /
    #\ / /| . ' .) \ /#
    | \ / )   , / \ / |
     \,/ ;;,,;,;   \,/
      _,#;,;;,;,
     /,i;;;,,;#,;
    //  %;;,;,;;,;
   ((    ;#;,;%;;,,
  _//     ;,;; ,#;,
 /_)      #,;    ))
         //      \|_
         \|_      |#\
          |#\      -"
'''


class Seller(Unit):
    pass
    # TODO: Добавить продавца

class BattleAction:
    ATTACK = 1
    BLOCK = 2
    ABILITY = 3
    ESTUS = 4


class Battle:
    def __init__(self, player: Player, enemy: Enemy) -> None:
        # , console: Console
        self.player = player
        self.enemy = enemy
        # self.console = console_


    def fight(player: Player, enemy: Enemy):
        turn = 1  # Порядок хода
        player_condition = True  # True = Life; False - Death
        player_armor_status = False
        enemy_armor_status = False
        while player.current_health > 0 and enemy.current_health > 0:
            print(f"\nHP {enemy.current_health} | ARMOR {enemy.base_armor}")
            print(f"HP: {player.current_health} | ARMOR {player.base_armor}\n")
            turn += 1
            if turn % 2 == 0:  # Мой ход
                enemy_solution = random.randint(1, 3)

                if enemy_solution == BattleAction.ATTACK:
                    print(f"Enemy prepares to attack")
                elif enemy_solution == BattleAction.BLOCK:
                    print(f"Enemy prepares to blocked")
                elif enemy_solution == BattleAction.ABILITY:
                    print(f"Enemy prepares to apply the ability")

                # player_solution = self.console.get_char()
                player_solution = int(input(f"Твой ход: "))
                if player_solution == BattleAction.ATTACK:
                    dice = random.randint(1, 20)
                    if dice == 1:
                        print(f"Attack is missed")
                    elif 2 <= dice <= 15:
                        enemy.get_damage(player.real_attack)
                    elif 16 <= dice <= 20:
                        enemy.get_damage(player.real_attack)

                    if enemy.current_health <= 0:  # Смерть врага
                        player.level_up(enemy.exp_after_death)
                        player.money += enemy.money_after_death
                        print(f"Победил игрок")
                        return player_condition

                if player_solution == BattleAction.BLOCK:
                    player.base_armor += 5  # TODO: Добавить фукнцию для брони
                    player_armor_status = True

                if player_solution == BattleAction.ESTUS:
                    player.regeneration_health(10)

                if player_solution == BattleAction.ABILITY:
                    pass
                    # TODO: добавить действия связанные с механикой героя

                if enemy_armor_status:
                    enemy.base_armor -= 5
                    enemy_armor_status = False


            elif turn % 2 != 0:  # Ход врага
                if enemy_solution == BattleAction.ATTACK:
                    dice = random.randint(1, 20)
                    if dice == 1:
                        print(f"Attack is missed")
                    elif 2 <= dice <= 15:
                        player.get_damage(enemy.real_attack)
                    elif 16 <= dice <= 20:
                        player.get_damage(2 * enemy.real_attack)

                    if player.current_health <= 0:
                        player_condition = False
                        print(f"Победил враг")
                        return player_condition

                if enemy_solution == BattleAction.BLOCK:
                    enemy.base_armor += 5
                    enemy_armor_status = True

                if enemy_solution == BattleAction.ABILITY:
                    pass
                    # TODO: добавить действия связанные с механикой героя

                if player_armor_status:
                    player.base_armor -= 5
                    player_armor_status = False


if __name__ == '__main__':
    me = Player(Console())

    me.inventory.show_inventory()
    for i in range(10):
        enemy = Demon()
        b = Battle.fight(me, enemy)
        print(f'Результат: {b}')
