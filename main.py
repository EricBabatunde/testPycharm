import random


playerhp = 275
enemyatkl = 25
enemyatkh = 50

while playerhp > 0:
    damage = random.randrange(enemyatkl, enemyatkh)
    playerhp -= damage

    if playerhp <= 30:
        playerhp = 30

    print("Enemy attacks with", damage, "points and new player HP is", playerhp, ".")

    if playerhp > 30:
        continue

    print("You are nearly dead.")
    break