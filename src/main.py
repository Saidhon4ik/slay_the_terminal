import random
from enemies import SmartEnemy

player_hp = 40
block = 0

enemy = SmartEnemy("Mr.Squidward", 40)
is_playing = True


def enemy_attack_player(block, player_hp):
    damage = random.randint(4, 9)

    damage = max(0, damage - block)
    block = 0

    player_hp -= damage
    player_hp = max(0, player_hp)

    return block, player_hp, damage


def player_block():
    return random.randint(4, 6)


def skip_turn():
    print("You skipped turn")


while is_playing:
    print("======================")
    print(f"{enemy.name}'s HP: {enemy.hp}")
    print(f"Your HP: {player_hp}")
    print(f"Block: {block}")
    print("======================")
    print("q. Quit")
    print("0. Skip turn")
    print("1. Attack (6 dmg)")
    print("2. Block")
    print("======================")

    choice = input("Choice: ").lower()

    # ================= ATTACK =================
    if choice == "1":
        enemy.hp -= 6
        enemy.hp = max(0, enemy.hp)

        if enemy.hp == 0:
            print(f"{enemy.name} was killed")
            print("You won")
            break

        block, player_hp, damage = enemy_attack_player(block, player_hp)

        print(f"You attacked {enemy.name}. HP left: {enemy.hp}")
        print(f"He dealt {damage} damage.")

    # ================= SKIP =================
    elif choice == "0":
        skip_turn()
        block, player_hp, damage = enemy_attack_player(block, player_hp)
        print(f"{enemy.name} dealt {damage} damage.")

    # ================= BLOCK =================
    elif choice == "2":
        block += player_block()
        print("You raised block")

        block, player_hp, damage = enemy_attack_player(block, player_hp)

        print(f"Block now: {block}")
        print(f"{enemy.name} dealt {damage} damage.")

    # ================= QUIT =================
    elif choice == "q":
        print("You ran away")
        break

    # ================= DEATH =================
    if player_hp == 0:
        print("You DIED")
        break

print("Game over")
