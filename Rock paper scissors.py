import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    print("Welcome to Rock, Paper, Scissors!")

    play_again = True
    while play_again:
        print("\nChoose one: Rock, Paper, Scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in choices:
            print("Please enter a valid choice (rock, paper, or scissors).")
            continue
        computer_choice = random.choice(choices)

        print(f"\nYour choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "you win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Your score: {user_score} | Computer's score: {computer_score}")
        play = input("\nDo you want to play again? (yes/no): ").lower() 
        if play != 'yes':
            play_again = False


        print("\nThanks for playing!")

if __name__ == "__main__":
    main()                   