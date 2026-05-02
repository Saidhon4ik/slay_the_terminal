from combat import start_combat
from player import Player
from enemy import Enemy
from enemies import Goblin,Gigachad,Slime

def main():
    print("=========================================")
    print("Welcome to the Slay The Terminal")
    print("It is a fanmade game, so have fun")
    print("=========================================\n")


    name = input("Enter your name: ")
    name = name.strip()


    while not name or not name.replace("_", "").isalpha():
        print("Please try again")
        name = input("Enter your name: ")
        name = name.strip()

    player = Player(name)
    enemies = [
        Slime(),
        Goblin(),
        Gigachad()
    ]

    for enemy in enemies:
        print(f"The {enemy.name} has woken up. Get ready to fight")     
        start_combat(player,enemy)
        if enemy != enemies[-1]:
            player.heal()


if __name__ == "__main__":
    main()