import random

class Enemy:
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"Raaaawrrrrr!!!!!!!!! Im dangeroussss I'm a {self.__type_of_enemy}!!!!!!")
    def walks_foward(self):
        print(f"{self.__type_of_enemy} is moving closer to you!!!! Run!!!")
    def attack(self):
        print(f"{self.__type_of_enemy} attacked you! With {self.attack_damage} damage!!!!")
    def get_type_of_enemy(self):
        return self.__type_of_enemy
    def special_attack(self):
        print("The enemy has no special attack!")


class Zombie(Enemy):
    def __init__(self,health_points, attack_damage):
        super().__init__(type_of_enemy = "Zombie", health_points=health_points, attack_damage=attack_damage)
    def talk(self):
        print("Grumblinggg....!!!!!")
    def special_attack(self):
        special_attack_work = random.random() < 0.5
        if special_attack_work:
            self.health_points += 2
            print("Zombie recovered 2 HP health!")

class Ogre(Enemy):
    def __init__(self,health_points, attack_damage):
        super().__init__(type_of_enemy = "Ogre", health_points=health_points, attack_damage=attack_damage)
    def talk(self):
        print("Ogre is slamming....!!!!!")
    def special_attack(self):
        special_attack_work = random.random() < 0.2
        if special_attack_work:
            self.attack_damage += 4
            print("Ogre had your attack damage increased by 4!!!!")






