class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Armor(Item):
    def __init__(self, name, description, item_armor):
        super().__init__(name, description)
        self.item_armor = item_armor

class Weapon(Item):
    def __init__(self, name, description, item_damage):
        super().__init__(name, description)
        self.item_damage = item_damage

class Potion(Item):
    def __init__(self, name, description, duration):
        super().__init__(name, description)
        self.duration = duration

class Healing_Potion(Potion):
    def __init__(self, name, description, duration):
        super().__init__(name, description, duration)


class Damage_Potion(Potion):
    def __init__(self, name, description, duration):
        super().__init__(name, description, duration)



Assault_cuirass = Armor("Штурмовая кираса", "Тяжелая броня, покрытая кроваво-красной краской", 30)
Shivas_guard = Armor("Броня Шивы", "Изысканный доспех, сделанный из черного металла, украшенный кристаллами и ониксом", 20)
Blade_mail = Armor("Кольчуга с лезвием", " Кираса из черной драконьей чешуи", 15)

Blood_kings_blade = Weapon(" ", "Меч, пропитанный кровью врагов", 20)
Fallen_angel_bow = Weapon("Лук Падшего Ангела", "Лук, который поражает душу врага", 18)
Black_warrior_axe = Weapon("Топор Черного Воина", "Топор, насыщенный злом и жаждой убийств", 32)

Healing_potion = Potion("Зелье исцеления", "Это зелье восстанавливает немного здоровья, помогая вам пережить трудные битвы", 15)