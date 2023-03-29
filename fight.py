import random
from typing import List
from enum import Enum
from items import Item, Weapon, Armor, Healing_Potion, Potion, Damage_Potion
# from console import Console
class Unit:
    def __init__(self) -> None:
        self.max_health = 100
        self.current_health = self.max_health

        self.base_attack = 10
        self.real_attack = self.base_attack

        self.base_armor = 10
        self.additional_armor = 0

        # self.agility = 10

        self.estus = 3  # TODO: ??? 인벤토리로 이동 ???
        self.weapon = None
        self.armor = None

    # Конечная функция, которая наносит урон
    def get_damage(self, attack) -> None:
        self.current_health -= attack * self.get_real_damage()

    # def get_total_armor(self):
    #     if self.armor:
    #         return self.additional_armor + self.base_armor + self.armor.item_armor
    #     else:
    #         return self.additional_armor + self.base_armor

    # Функция, которая возвращает множитель, чтобы уменьшить урон, в зависимости от количества брони
    def get_real_damage(self):
        # full_armor = self.get_total_armor()
        full_armor = self.base_armor + self.additional_armor
        damage_multiplier = 1 - ((0.06 * full_armor) / (1 + 0.06 * abs(full_armor)))
        return damage_multiplier

    # def get_real_attack(self):
    #     if self.weapon:
    #         return self.base_attack + self.weapon.item_damage
    #     else:
    #         return self.base_attack

class Player(Unit):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.money = 0
        self.exp_for_level = 10
        self.current_exp = 0
        # self.effects: List[Effect] = []
    def level_up(self, experience) -> None:
        self.current_exp += experience
        if self.current_exp >= self.exp_for_level:
            # Если опыта набралось нужное кол-во для поднятия уровня, то поднимаем уровень и кол-во exp для нового уровня
            self.current_exp = self.current_exp - self.exp_for_level
            self.level += 1
            self.exp_for_level = self.level * 10

    # def potions_actions(self):
    #     for potion in self.effects:
    #         if potion.duration > 0:
    #             self.real_attack = self.base_attack + potion.value * len(filter(lambda effect: effect.duration > 0 and effect.name == potion.name))


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

        while player.current_health > 0 and enemy.current_health > 0:
            enemy.additional_armor -= 5
            player.additional_armor -= 5
            print(f"\nХп врага: {enemy.current_health}, общая броня врага: {enemy.additional_armor + enemy.base_armor}")
            print(f"Мой хп: {player.current_health}, моя общая броня: {player.additional_armor + player.base_armor}\n")
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
                    player.additional_armor += 5  # TODO: Добавить фукнцию для брони

                if player_solution == BattleAction.ESTUS:
                    difference_in_health = player.max_health - player.current_health
                    if difference_in_health >= 10 and player.estus > 0:
                        player.current_health += 10
                        player.estus -= 1
                    elif difference_in_health < 10 and player.estus > 0:
                        player.current_health += difference_in_health
                        player.estus -= 1

                if player_solution == BattleAction.ABILITY:
                    pass
                    # TODO: добавить действия связанные с механикой героя


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
                    enemy.additional_armor += 5

                if enemy_solution == BattleAction.ABILITY:
                    pass
                    # TODO: добавить действия связанные с механикой героя

me = Player()
enemy = Demon()
Battle = Battle.fight(me, enemy)
