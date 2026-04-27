import random

player_hp = 40
shield = 0 
mob_hp  = 40
mob1_name = "Mr.Squidward"
is_playing = True

while is_playing:
    print("======================")
    print(f"{mob1_name}'s HP: {mob_hp}")
    print(f"Your HP: {player_hp}")
    print(f"Shield: {shield}")
    print("======================")
    print("q. Quit the game")
    print("0. Skip turn")
    print("1. Attack (deal 6 damage)")
    print("2. Use the shield")
    print("======================")

    choice = input("Enter your choice: ").lower()

    # =========================
    # ATTACK
    # =========================
    if choice == "1":
        mob_hp -= 6
        mob_hp = max(0, mob_hp)

        if mob_hp == 0:
            print(f"{mob1_name} was killed")
            print("Congratulations, you won")
            is_playing = False
            continue

        # ENEMY ATTACK
        damage = random.randint(4, 9)

        if shield >= damage:
            shield -= damage
            damage = 0
        else:
            damage -= shield
            shield = 0

        player_hp -= damage
        player_hp = max(0, player_hp)

        print(f"You attacked {mob1_name}. It has {mob_hp} HP left")
        print(f"{mob1_name} dealt {damage} damage.")

        if player_hp == 0:
            print("You DIED. GAME OVER")
            is_playing = False

    # =========================
    # SKIP TURN
    # =========================
    elif choice == "0":
        print("You skipped your turn")

        damage = random.randint(4, 9)

        if shield >= damage:
            shield -= damage
            damage = 0
        else:
            damage -= shield
            shield = 0

        player_hp -= damage
        player_hp = max(0, player_hp)

        print(f"{mob1_name} dealt {damage} damage. You have {player_hp} HP")

        if player_hp == 0:
            print("You DIED. GAME OVER")
            is_playing = False

    # =========================
    # SHIELD
    # =========================
    elif choice == "2":
        print("You raised your shield")
        shield += random.randint(4, 6)
        print(f"Shield is now {shield} points")

        damage = random.randint(4, 9)

        if shield >= damage:
            print(f"{mob1_name} attacked you and dealt {damage} danage, but shield blocked all of that damage")
            shield -= damage
            damage = 0
            
        else:
            damage -= shield
            shield = 0
            player_hp -= damage
            player_hp = max(0, player_hp)

            print(f"{mob1_name} dealt {damage} damage. You have {player_hp} HP")

        if player_hp == 0:
            print("You DIED. GAME OVER")
            is_playing = False

    # =========================
    # QUIT
    # =========================
    elif choice == "q":
        print("You ran away from battle.")
        is_playing = False

    else:
        print("Invalid choice")

print("Thanks for playing!")
