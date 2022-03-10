import random
import time

random.seed(time.time())

 # enemy stat modifier for walk/dash
 # items ( dictionary )
 # enemy drop items gold?
 # item shop?



class character():
    def __init__(self, name, strength, defense, current_health, max_health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.current_health = current_health
        self.max_health = max_health
        self.items = {}
    # object is attacking argument
    def attack(self, defender):
        damage = defender.defense - self.strength
        if damage < 0:
            return  damage
        else:
            return 0
    # object is defending attack from arguement
    def defend(self, attacker):
        print(f"{self.name} Defends")
        damage = round((self.defense - attacker.strength)/1.2)
        if damage < 0:
            print(f"{damage} Damage to {self.name}")
            return damage
        else:
            print(f"0 Damage to {self.name}")
            return 0

hero_name = input("Hero Name:")
print("Distribute 10 talent points")
print("Leftover points from Strength will become Defense")
talent = 10
attack_counter = 0
defense_counter = 0
health_counter = 0
days = 0
distance = 0

while True:
    try:
        hero_strength = int(input("Stength:"))
        if hero_strength > 0 and hero_strength < 10:
            break
    except:
        print("Stength value needs to be 1-9")

hero_defense = talent - hero_strength

hero = character(hero_name, hero_strength, hero_defense, 10, 10)
def print_stats(character_name):
    print(f"Name: {character_name.name} Strength: {character_name.strength} \
    Defense: {character_name.defense} Current Health: {character_name.current_health} \
    Max Health: {character_name.max_health}")

print_stats(hero)

def enemy_stat_range():
    return round((hero.defense + hero.strength)/1.5)


while True:

    enemy_strength = round(random.randint(1, enemy_stat_range()))
    enemy_defense = round(random.randint(1, enemy_stat_range()))
    enemy_health = round(random.randint(1, enemy_stat_range()))
    monster = character("goblin", enemy_strength, enemy_defense, enemy_health, enemy_health)
    encounter_rate = 0

    action = input(" walk - dash - rest - status ")
    if action == "walk":
        days += 1
        distance += 1
        encounter_rate = 50

    if action == "dash":
        days += 1
        distance +=2
        encounter_rate = 70

    if action == "rest":
        print("Resting has done your body good. Your health is full")
        health_counter += (hero.max_health - hero.current_health)
        hero.current_health = hero.max_health
        days += 1

    if action == "status":
        print_stats(hero)
    # hero must cause damage during attack or receive damage during defend to activate counter
    print(f"Encounter Rate {random.randint(1,100)}")
    if (random.randint(1,100)<encounter_rate):
        print_stats(monster)
        print(" You've encountered a monster!")
        while monster.current_health >0:
            fight = input("attack - defend - run  ")
            if fight == "attack":
                damage= monster.attack(hero)
                hero.current_health= hero.current_health + damage
                print(f"{monster.name}causes {damage} damage to {hero.name}")
                damage = hero.attack(monster)
                print(f"{hero.name} causes {damage} damage to {monster.name}")
                monster.current_health = monster.current_health + damage
                if damage < 0:
                    attack_counter += 1
                print(f"{hero.name} Health:{hero.current_health}")
                if hero.current_health == None or hero.current_health < 1:
                    print("You've been defeeated...\n\
                        Local Villagers find you and nurse you back to health.\n \
                        Being bedridden for 7 days has made you weaker than you once were..")
                    days += 7
                    attack_counter = 0
                    defense_counter = 0
                    health_counter = 0
                    hero.strength -= 1
                    hero.defense -= 1
                    hero.max_health -= 1
                    hero.current_health = hero.max_health
                    break
                if monster.current_health == None or monster.current_health <= 0:
                    print(f"{monster.name} Defeated!")
                    break
                print(f"{monster.name} Health:{monster.current_health}")

            if fight == "defend":
                damage=hero.defend(monster)
                hero.current_health= hero.current_health + damage
                print(f"{monster.name} causes {damage} damage to {hero.name}")
                if damage < 0:
                    defense_counter += 1
                print(f"{hero.name} Health:{hero.current_health}")
                print(f"{monster.name} Health:{monster.current_health}")

            if fight == "run":
                attack_counter = 0
                defense_counter = 0
                health_counter = 0
                print("You had decided to run... Fear of this monster haunt you\n \
                    You have lost precious adventure experience...")
                break
    print(f"Day {days} on your Journey \n Distance {distance} miles")

    if attack_counter >= 5 :
        hero.strength += 1
        attack_counter = 0
        print("Attacking Monsters has made you deadlier...\n Strength +1")

    if defense_counter >= 5:
        hero.defense += 1
        defnese_counter = 0
        print("Defending against monsters has toughed you up...\nDefense +1")

    if health_counter >= round(hero.max_health /2):
        hero.max_health += 1
        defense_counter = 0
        print(" Your wounds have healed and made your body more fortified...\n Max Health +1")
