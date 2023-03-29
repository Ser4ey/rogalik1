class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Armor(Item):
    def __init__(self, name, description, item_armor, price):
        super().__init__(name, description)
        self.item_armor = item_armor
        self.price = price

class Weapon(Item):
    def __init__(self, name, description, item_damage, price):
        super().__init__(name, description)
        self.item_damage = item_damage
        self.price = price

class Potion(Item):
    def __init__(self, name, description, duration, price):
        super().__init__(name, description)
        self.duration = duration
        self.price = price

class Healing_Potion(Potion):
    def __init__(self, name, description, duration, price):
        super().__init__(name, description, duration)
        self.price = price


class Damage_Potion(Potion):
    def __init__(self, name, description, duration, price):
        super().__init__(name, description, duration)
        self.price = price



Assault_cuirass = Armor("Штурмовая кираса", "Тяжелая броня, покрытая кроваво-красной краской", 30, 50)
Shivas_guard = Armor("Броня Шивы", "Изысканный доспех, сделанный из черного металла, украшенный кристаллами и ониксом", 20, 30)
Blade_mail = Armor("Кольчуга с лезвием", " Кираса из черной драконьей чешуи", 15, 20)

Blood_kings_blade = Weapon(" ", "Меч, пропитанный кровью врагов", 20, 10)
Fallen_angel_bow = Weapon("Лук Падшего Ангела", "Лук, который поражает душу врага", 18, 9)
Black_warrior_axe = Weapon("Топор Черного Воина", "Топор, насыщенный злом и жаждой убийств", 32, 20)

Healing_potion = Potion("Зелье исцеления", "Это зелье восстанавливает немного здоровья, помогая вам пережить трудные битвы", 15, 10)