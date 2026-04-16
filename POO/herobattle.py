from enemy import *

class Weapon:
    def __init__(self, weapon_type, attack_increased):
        self.weapon_type = weapon_type
        self.attack_increased = attack_increased


class Hero:
    def __init__(self, health_points, attack_damage):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon: Weapon = None

    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increased
            self.is_weapon_equipped = True
    def talk(self):
        print("I'll Win!!!!")
    def attack(self):
        print("Hero is attacking!")

def battle(h1:Hero, e2: Enemy):
    h1.talk()
    e2.talk()
    while h1.health_points > 0 and e2.health_points > 0:
        print('----------')
        e2.special_attack()
        print(f'Hero: {h1.health_points} health points left!')
        print(f'{e2.get_type_of_enemy()}: {e2.health_points} health points left!')
        h1.attack()
        e2.health_points -= h1.attack_damage
        e2.attack()
        h1.health_points -= e2.attack_damage

    print('----------')
    if h1.health_points <= 0 and e2.health_points > 0:
        print(f'{e2.get_type_of_enemy()} wins!')
    elif h1.health_points > 0 and e2.health_points <= 0:
        print('Hero Wins')
    else:
        print('Draw!!')


zombie = Zombie(10, 1)
Ogre = Ogre(30, 2)
hero = Hero(10, 1)
weapon = Weapon('Sword', 8)
hero.weapon = weapon
hero.equip_weapon()
battle(hero, Ogre)