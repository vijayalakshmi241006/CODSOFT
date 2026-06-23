import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Rock beats scissors, scissors beat paper, and paper beats rock
    if user_choice == computer_choice:
        return "tie"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    
    print("=" * 40)
    print("    CODSOFT ROCK-PAPER-SCISSORS GAME    ")
    print("=" * 40)
    print("Rules: Rock beats Scissors | Scissors beat Paper | Paper beats Rock")
    
    while True:
        # User Input
        user_choice = input("\nChoose rock, paper, or scissors: ").strip().lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose either 'rock', 'paper', or 'scissors'.")
            continue
        
        # Computer Selection
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # Game Logic & Score Tracking
        result = determine_winner(user_choice, computer_choice)
        
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        # Display Current Score
        print(f"--- Score Board --- You: {user_score} | Computer: {computer_score}")
        
        # Play Again loop
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes' and play_again != 'y':
            print("\n" + "=" * 40)
            print("           FINAL GAME OVER            ")
            print(f"Final Scores -> You: {user_score} | Computer: {computer_score}")
            print("Thank you for playing! Goodbye.")
            print("=" * 40)
            break

if __name__ == "__main__":
    play_game()
