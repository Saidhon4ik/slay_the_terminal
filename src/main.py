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
    enemy1 = Enemy("Slime",40,6)

    start_combat(player, enemy1)


if __name__ == "__main__":
    main()