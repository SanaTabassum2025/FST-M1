while True:
    player1 = input("Enter a choice from (rock, paper, scissors): ").lower()
    player2 = input("Enter a choice from (rock, paper, scissors): ").lower()

    if player1 == player2:
        print("Tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Player1 wins")
        else:
            print("Player2 wins")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player1 wins")
        else:
            print("Player2 wins")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player1 wins")
        else:
            print("Player2 wins")
    else:
        print("Invalid input. Please choose rock, paper, or scissors.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break



