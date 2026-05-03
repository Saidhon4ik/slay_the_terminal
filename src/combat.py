from player import Player
from enemy import Enemy

def start_combat(player, enemy):  # passing the objects
    turn = 0
    while player.is_alive() and enemy.is_alive():
        player.deck.draw(4)
        for i, card in enumerate(player.deck.hand):
            print(f"{i+1}. {card.name} - {card.description}")
        enemy.take_action()
        print("\n\n================================")
        print(f"{player.name}'s hp: {player.hp}/{player.max_hp}")
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


        choice = int(choice)
        if choice == 1:
            actual_damage = max(0,player.damage - enemy.block)
            block_amount = player.damage - actual_damage
            player.deal_damage(enemy)    
            if enemy.dodge:
                pass
            else:
                
                if block_amount > 0:
                    print(f"{player.name} attacks for {player.damage}. {enemy.name} has blocked {block_amount}. {enemy.name} takes {actual_damage} damage")
                else:
                    print(f"You dealt {actual_damage} damage to {enemy.name}!")
    



        elif choice == "2":
            player.add_block(5)


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

        

        enemy.execute_action(player,turn)   

        if not player.is_alive():
            print("================================")
            print(f"{player.name} was defeated by a {enemy.name}")
            print("You have lost the battle")
            print("You LOST")
            print("================================")
            break


        player.deck.discard_hand()
        turn += 1
        player.block = 0
        enemy.block = 0