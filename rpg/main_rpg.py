from rpg.classes.game_cl import Person, bcolors
from rpg.classes.magic import Spell


# Black magic
Fire = Spell("Fire", 15, 100, "black")
Thunder = Spell("Thunder", 18, 144, "norse")
Blizzard = Spell("BLizzard", 25, 175, "black")
Meteor = Spell("Meteor", 30, 200, "white")
Quake = Spell("Quake", 10, 90, "mage")

# white magic
Cure = Spell("Cure", 15, 100, "white")
Cura = Spell("Cura", 20, 200, "white")


player = Person(460, 65, 60, 34, [Fire, Thunder, Blizzard, Meteor, Quake, Cure, Cura])

enemy1 = Person(1200, 65, 45, 25, [])

running = True
i = 0

while running:
    print("==============================")
    player.choose_action()
    choice = input("Choose an action: ")
    choice_index = int(choice) - 1

    if choice_index == 0:
        dmg = player.generate_attackdmg()
        enemy1.take_damage(dmg)
        enemy_currenthp = enemy1.get_hp()

        print(bcolors.OKBLUE + "Player deals", dmg, "points of damage!!" + bcolors.ENDC)

    elif choice_index == 1:
        player.choose_spell()
        spell_choice = int(input("Choose a spell: ")) - 1

        chosen_spell = player.magic[spell_choice]
        magic_dmg = chosen_spell.generate_dmg()
        spell_name = chosen_spell.name
        spell_cost = chosen_spell.cost

        player_currenthp = player.get_hp()
        player_currentmp = player.get_mp()

        if spell_cost > player_currentmp:
            print(bcolors.FAIL + "\nNot enough MP!\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell_cost)

        if chosen_spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "Player heals", magic_dmg, "points of HP!!" + bcolors.ENDC)
        elif chosen_spell.type == "black":
            enemy1.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\nPlayer used", spell_name, "to deal", magic_dmg, "points of damage!!" + bcolors.ENDC)

    enemy_dmg = enemy1.generate_attackdmg()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + "Enemy deals", enemy_dmg, "points worth of damage" + bcolors.ENDC)

    print("--------------------------------")
    print(bcolors.FAIL + "Enemy HP:", str(enemy1.get_hp()) + "/" + str(enemy1.get_max_hp()) + bcolors.ENDC)

    print(bcolors.OKBLUE + "Player HP:", str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print(bcolors.OKBLUE + "Player MP:", str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy1.get_hp() <= 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False

    elif player.get_hp() <= 0:
        print(bcolors.FAIL + "You lose! Your enemy has defeated you!" + bcolors.ENDC)
        running = False
