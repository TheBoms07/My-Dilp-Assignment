print("PLAY WITH THE BOMS")

name = input("What is your full name: ")

players_role = input("Enter your character in the game (Rock, Paper, Scissors): ")
computer_role = Random.choice(["rock","paper","scissors"])

game_level = input("Enter your desired level (Easy or Hard): ")

if players_role == computer_role:
    elif 