from player import Player
from enemy import Enemy


def start_combat(player, enemy):  # passing the objects
    while player.is_alive() and enemy.is_alive():
        print("\n================================")
        print(f"Player's hp: {player.hp}/{player.max_hp}")
        print(f"Player's current block: {player.block}")
        print("================================\n")

        print("\n================================")
        print(f"Enemy's hp: {enemy.hp}/{enemy.max_hp}")
        print(enemy.get_intent())
        print("\n================================")

        print("\n================================")
        print("\nWhat do you do?")
        print("1. Attack")
        print("2. Block")
        print("3. Skip")
        choice = input("> ")
        print("================================\n")

        if choice == "1":
            player.deal_damage(enemy)
        
        elif choice == "2":
            player.add_block(5)

        elif choice == "3":
            player.skip_turn()
        else:
            print("You gotta choose a valid option")
            continue


        if not enemy.is_alive():
            print("\n================================")
            print(f"{enemy.name} was defeated by powerful {player.name}")
            print("You have won the battle")
            print("You WON")
            print("================================\n")
            break

        player.take_damage(enemy.damage)


        if not player.is_alive():
            print("\n================================")
            print(f"{player.name} was defeated by a {enemy.name}")
            print("You have lost the battle")
            print("You LOST")
            print("================================\n")
            break
