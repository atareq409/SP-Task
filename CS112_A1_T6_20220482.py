# Description: this game has a board of 3*3 places and each player has his own numbers (odd and even) and each player is trying to reach a total of 15 in the rows
# Author: Abdallah Tarek Eid (20220482)
# Version: Task 6 game number 2 
# Date : 3/3/2024


def play_board(board):  # This is made to draw a board for the players
    for row in board:
        print(" | ".join(map(str, row)))   # map is made to repeat the symbol "|" through rows
        print("-" * 9)     # this is made to divide the game into three rows

def check_winner15(board):
    for i in range(3):   # This is made to check rows, columns, and diagonals
        if sum(board[i]) == 15 or sum(board[j][i] for j in range(3)) == 15:
            return True
    if board[0][0] + board[1][1] + board[2][2] == 15 or board[0][2] + board[1][1] + board[2][0] == 15:
        return True
    return False

def play_game():
    board = [[0, 0, 0] for _ in range(3)]
    print("Welcome to FCAI-CU Tic-Tac-Toe Game ")
    print("Please enter your names.")    # this is made to take the players name as an input
    player_one_name = input("Enter player one's name: ") 
    player_two_name = input("Enter player two's name: ")
    play_board(board)
    current_player = player_one_name   # this is made to start the game with player 1 (who is using odd numbers)

    for _ in range(9):
        while True:
            try:
                num = int(input(f"{current_player}, please enter your number (0-9): "))  # displaying a message of the range of numbers
                if num < 0 or num > 9:                  # this is made to make the range of available numbers from 0 to 9
                    print("Invalid number. Please enter a number between 0 and 9.")  
                    continue
                if (current_player == player_one_name and num % 2 == 0) or (current_player == player_two_name and num % 2 != 0):  # this is made to validate player one with odd numbers only and player two with even numbers only
                    print("Invalid number. Odd numbers for", player_one_name, "even numbers for", player_two_name)
                    continue
                break
            except ValueError:     # this is made to prevent the players to input a string
                print("Invalid input. Please enter a valid number.")

        if any(num in row for row in board):  # this is made to prevent the repeating of the chosen numbers
            print("This number is already taken. Please choose another number: ")
            continue
 
        for i in range(3):  # This is made to assign numbers to players
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = num
                    break
            else:
                continue
            break

        play_board(board)

        if check_winner15(board):   # this is made to check if the sum of the row is 15 or not
            print(f"{current_player} wins!")
            return

        current_player = player_two_name if current_player == player_one_name else player_one_name  # this is made to switch players

    print("It's a draw.")   # this is made to display a draw if the sum of the two players don't equal 15.

if __name__ == "__main__":
    play_game()
