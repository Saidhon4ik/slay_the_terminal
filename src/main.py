from combat import start_combat
from player import Player
from enemy import Enemy

def main():
    print("=========================================")
    print("Welcome to the Slay The Terminal")
    print("It is a fanmade game, so have fun")
    print("=========================================\n")


    name = input("Enter your name: ")
    name = name.strip()


    while not name:
        print("Name cannot be empty bro...")
        name = input("Enter your name: ")
        name = name.strip()

    player = Player(name)
    enemies = [
        Enemy("Slime",20,4),
        Enemy("Goblin",30,6),
        Enemy("Mr.Gigachad",50,8)
    ]

    for enemy in enemies:
        print(f"The {enemy.name} has woken up. Get ready to fight")     
        start_combat(player,enemy)
        if enemy != enemies[-1]:
            player.heal()


if __name__ == "__main__":
    main()