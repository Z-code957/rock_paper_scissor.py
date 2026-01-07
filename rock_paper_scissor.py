import random

def get_user_choice():
    print("\nChoose one: rock, paper, or scissors")
    choice = input("Your choice: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Your choice: ").lower()
    return choice

def get_ai_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, ai):
    if user == ai:
        return "It's a tie!"
    elif (user == "rock" and ai == "scissors") or \
         (user == "paper" and ai == "rock") or \
         (user == "scissors" and ai == "paper"):
        return "You win!"
    else:
        return "AI wins!"

def play_game():
    print("=== Rock, Paper, Scissors ===")
    while True:
        user_choice = get_user_choice()
        ai_choice = get_ai_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"AI chose: {ai_choice}")

        print(determine_winner(user_choice, ai_choice))

        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()