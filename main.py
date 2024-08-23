from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} изменяет оружие.")

    def attack_monster(self, monster):
        print(self.weapon.attack())
        monster.defeated()

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name

    def defeated(self):
        print(f"{self.name} побежден!")

# Шаг 4: Демонстрация боя
# Создаем монстра
monster = Monster("Скелет")

# Создаем бойца с мечом
fighter = Fighter("Воин", Sword())
print(f"Боец выбирает меч.")
fighter.attack_monster(monster)

# Боец меняет меч на лук
fighter.change_weapon(Bow())
print(f"Боец выбирает лук.")
fighter.attack_monster(monster)