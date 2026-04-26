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
        mob_hp = max(0,mob_hp) #number cant go below 0

        mob1_attack = random.randint(4,9)
        

        if mob_hp == 0:        
            print(f"{mob1_name} was killed")
            print("Congratulations, you won")
            is_playing = False
        else:
            if shield > mob1_attack:
                shield -= mob1_attack
            else:
                mob1_attack -= shield
                player_hp -= mob1_attack
                print(f"Enemy dealt {mob1_attack} damage to you this turn cuz of your block")
                
            player_hp = max(0, player_hp) #hp cant go below 9o
            print(f"You attacked {mob1_name}. Now, it has {mob_hp} hp ")
            print(f"{mob1_name} dealt {mob1_attack} damage. Now you have {player_hp} hp")
            if player_hp == 0:
                print("You DIED. GAME OVER")
                is_playing = False

    elif choice == "0":
        print("You skip your turn")

        mob1_attack = random.randint(4, 9)
        player_hp -= mob1_attack
        player_hp = max(0, player_hp)

        print(f"{mob1_name} attacks you while you skip. You have {player_hp} HP")

        if player_hp == 0:
            print("You died")
            print("GAME OVER")
            is_playing = False

    elif choice == "2":
        print("You decided to use shield")
        shield += random.randint(4,6)
        print(f"Now you have {shield} poins of shield")


    elif choice == "q":
        print("You decided not to fight and ran away. You LOST")
        is_playing = False
    else:
        print("You choose a wrong option, please choose again")


print("Thanks for playing my mini-game , have a nice day")
