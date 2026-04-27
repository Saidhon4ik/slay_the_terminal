import random

player_hp = 40
shield = 0 
mob_hp  = 40
mob1_name = "Mr.Squidward"
is_playing = True

while is_playing:
    print("======================")
    print("q. Quit the game")
    print("0. Skip turn")
    print("1. Attack (deal 6 damage)")
    print("2. Use the shield")
    print("======================")

    choice = input("Enter your choice: ").lower()

    if choice == "1":
        mob_hp -= 6
        mob_hp = max(0, mob_hp)

        if mob_hp == 0:        
            print(f"{mob1_name} was killed")
            print("Congratulations, you won")
            is_playing = False
        else:
            mob1_attack = random.randint(4, 9)
            damage = mob1_attack

            # SHIELD LOGIC
            if shield >= damage:
                shield -= damage
                damage = 0
            else:
                damage -= shield
                shield = 0

            player_hp -= damage
            player_hp = max(0, player_hp)

            print(f"You attacked {mob1_name}. Now it has {mob_hp} hp")
            print(f"{mob1_name} dealt {damage} damage. Now you have {player_hp} hp")

            # reset shield after attack
            shield = 0

            if player_hp == 0:
                print("You DIED. GAME OVER")
                is_playing = False

    elif choice == "0":
        print("You skip your turn")

        mob1_attack = random.randint(4, 9)
        damage = mob1_attack

        # shield also works on skip
        if shield >= damage:
            shield -= damage
            damage = 0
        else:
            damage -= shield
            shield = 0

        player_hp -= damage
        player_hp = max(0, player_hp)

        

        print(f"{mob1_name} dealt {damage} damage. Now you have {player_hp} hp")

        # reset shield
        shield = 0

        if player_hp == 0:
            print("You died")
            print("GAME OVER")
            is_playing = False

    elif choice == "2":
        print("You decided to use shield")
        shield += random.randint(4, 6)
        print(f"Now you have {shield} points of shield")

        mob1_attack = random.randint(4, 9)
        damage = mob1_attack

        if shield >= damage:
            shield -= damage
            damage = 0
            print(f"your shield blocked all upcoming damage. You still have {player_hp}")
        else:
            damage -= shield
            shield = 0

            player_hp -= damage
            player_hp = max(0, player_hp)

            print(f"{mob1_name} dealt {damage} damage. Now you have {player_hp} hp")

            shield = 0
    elif choice == "q":
        print("You decided not to fight and ran away.")
        is_playing = False

    else:
        print("You chose a wrong option, please choose again")

print("Thanks for playing my mini-game, have a nice day")
