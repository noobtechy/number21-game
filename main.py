import random

def player_move(current_number):
    while True:
        try:
            move = int(input("Enter  move (1, 2, or 3) : "))
            if move in [1, 2, 3] and current_number + move <= 21:
                return move
            else:
                print(" opsie Invalid move. Try again. plzz ")
        except ValueError:
            print("ohh Please enter a number.")

def computer_move(current_number):
    move = random.randint(1, min(3, 21 - current_number))
    print(f"Computer move: {move}")
    return move

def play_game():
    current_number = 0
    print(" Welcome to the 21 Number Game! ")
    print(" Players take turns to add 1, 2, or 3 to the current number. ")
    print(" The player who reaches 21 wins! ")

    while current_number < 21:
        
        move = player_move(current_number)
        current_number += move
        print(f"Current number: {current_number}")
        if current_number >= 21:
            print("You win!")
            break

        
        move = computer_move(current_number)
        current_number += move
        print(f"Current number: {current_number}")
        if current_number >= 21:
            print("Computer wins!")
            break

if __name__ == "__main__":
    play_game()