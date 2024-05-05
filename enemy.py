import random

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        return self.damage

class EnemySpawner:
    def __init__(self, enemy_types):
        self.enemy_types = enemy_types

    def spawn_enemy(self):
        enemy_type = random.choice(self.enemy_types)
        if enemy_type == "Astroids":
            return Enemy("Astriods", 50, 10)
        elif enemy_type == "Ships":
            return Enemy("Ships", 70, 15)
        elif enemy_type == "Forign Objects":
            return Enemy("Orc", 100, 20)
        else:
            return None

enemy_types = ["Astroids", "Ships", "Forign Objects"]
spawner = EnemySpawner(enemy_types)

enemy = spawner.spawn_enemy()

if enemy:
    print(f"A wild {enemy.name} appears with {enemy.health} health and {enemy.damage} damage!")
else:
    print("No enemy spawned.")