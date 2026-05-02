from player import Player
from enemy import Enemy

def start_combat(player, enemy):  # passing the objects
    while player.is_alive() and enemy.is_alive():
        print("\n================================")
        print(f"Player's hp: {player.hp}/{player.max_hp}")
        print("================================")
        print(f"Enemy's hp: {enemy.hp}/{enemy.max_hp}")
        print(enemy.get_intent())
        print("================================")
        print("What do you do?")
        print("1. Attack")
        print("2. Block")
        print("3. Skip")
        choice = input("> ")
        print("================================")

        if choice == "1":
            player.deal_damage(enemy)
        
        elif choice == "2":
            player.add_block(5)
            print(f"Player's current block: {player.block}")

        elif choice == "3":
            player.skip_turn()
        else:
            print("You gotta choose a valid option")
            continue


        if not enemy.is_alive():
            print("================================")
            print(f"{enemy.name} was defeated by a {player.name}")
            print("You have won the battle")
            print("You WON")
            print("================================")
            break
        

        print(f"Enemy block before attack: {enemy.block}")
        enemy.take_action(player)   
        print(f"Enemy block before attack: {enemy.block}")

        if not player.is_alive():
            print("================================")
            print(f"{player.name} was defeated by a {enemy.name}")
            print("You have lost the battle")
            print("You LOST")
            print("================================")
            break



        player.block = 0
        enemy.block = 0