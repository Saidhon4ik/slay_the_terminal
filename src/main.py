

player_hp = 40
mob_hp  = 40
mob1_name = "Mr.Squidward"
is_playing = True

while is_playing:
    print("======================")
    print("1. Attack (deal 6 damage)")
    print("0. Quit")
    print("======================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        mob_hp -= 6       
        if mob_hp <= 0:
            mob_hp = 0
            print(f"{mob1_name} was killed")
            print("Congratulations, you won")
            is_playing = False
        print(f"You attacked {mob1_name}. Now, it has {mob_hp} hp ")
    elif choice == 0:
        pass
    else:
        print("You choose a wrong option, please choose again")
