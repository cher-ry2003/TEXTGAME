import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("Your goal is to reach the treasure hidden deep within.")
    time.sleep(1)
    print("Be careful! Your choices will determine your fate.")

def make_choice(options):
    print("\nChoose your action:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = int(input("Enter the number of your choice: "))
    return choice

def forest_path():
    print("\nYou start walking through the dense forest.")
    time.sleep(1)
    print("Ahead, you see two paths.")
    time.sleep(1)

    choice = make_choice(["Take the left path", "Take the right path"])

    if choice == 1:
        print("\nYou chose the left path.")
        time.sleep(1)
        print("You encounter a friendly guide.")
        time.sleep(1)
        print("The guide helps you navigate through the forest.")
        time.sleep(1)
    else:
        print("\nYou chose the right path.")
        time.sleep(1)
        print("You stumble upon a pack of wolves!")
        time.sleep(1)
        print("Quickly, you climb a tree to escape them.")
        time.sleep(1)
        print("After a while, the wolves lose interest and leave.")

def cave():
    print("\nYou reach a mysterious cave.")
    time.sleep(1)
    print("Inside, you find two tunnels.")
    time.sleep(1)

    choice = make_choice(["Enter the left tunnel", "Enter the right tunnel"])

    if choice == 1:
        print("\nYou chose the left tunnel.")
        time.sleep(1)
        print("You discover a treasure chest!")
        time.sleep(1)
        print("Congratulations! You found the treasure.")
    else:
        print("\nYou chose the right tunnel.")
        time.sleep(1)
        print("You encounter a giant spider!")
        time.sleep(1)
        print("It's a tough fight, but you manage to defeat the spider.")
        time.sleep(1)
        print("You find a hidden passage leading to the treasure.")

def main():
    introduction()
    forest_path()
    cave()

if __name__ == "__main__":
    main()
