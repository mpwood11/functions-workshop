import time

def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"~~~|~~~|~~~")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"~~~|~~~|~~~")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

def mark_board(board, row, col, current_player):
    board[row][col] = current_player
    return board

def change_player(current_player, p1_name, p2_name):
    if current_player == p1_name:
        return p2_name
    else:
        return p1_name


def board_has_winner(board, current_player):

    # Rows win game
    if board[0][0] == current_player and board[0][1] == current_player and board[0][2] == current_player:
        return True
    elif board[1][0] == current_player and board[1][1] == current_player and board[1][2] == current_player:
        return True
    elif board[2][0] == current_player and board[2][1] == current_player and board[2][2] == current_player:
        return True

    # Columns win game
    elif board[0][0] == current_player and board[1][0] == current_player and board[2][0] == current_player:
        return True
    elif board[0][1] == current_player and board[1][1] == current_player and board[2][1] == current_player:
        return True
    elif board[0][2] == current_player and board[1][2] == current_player and board[2][2] == current_player:
        return True

    # Diagonals win game
    elif board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
        return True
    elif board[2][0] == current_player and board[1][1] == current_player and board[0][2] == current_player:
        return True

    # No winner...yet
    else:
        return False

def space_is_free(board, row, col):
    return board[row][col] == '-'

def board_is_full(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True

def main():

    print("WELCOME TO THERMONUCLEAR WAR")
    t = 0
    while t <= 3:
        time.sleep(1)
        print(".")
        t += 1
    print("Just kidding, this is TIC TAC TOE")
    print("\n\n")

    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    p1_name = input("Enter Player 1's Name: ")
    p2_name = input("Enter Player 2's Name: ")
    p1_symbol = False
    p2_symbol = False
    while p1_symbol == False:
        p1_symbol = input(f"{p1_name}, what symbol would you like to use? ")
        if p1_symbol == '-':
            p1_symbol = input(f"{p1_name}, please choose a different symbol. ")
    while p2_symbol == False:
        p2_symbol = input(f"{p2_name}, what symbol would you like to use? ")
        if p2_symbol == ('-' or p1_symbol):
            p2_symbol = input(f"{p2_name}, please choose a different symbol. ")

    current_player = p1_name

    while True:
        print_board(board)

        while True:
            row = int(input(f"{current_player}, it's your turn. Pick a row 1-3.")) - 1
            col = int(input(f"Pick a column 1-3.")) - 1
            if space_is_free(board, row, col):
                break

        board = mark_board(board, row, col, current_player)

        if board_has_winner(board, current_player):
            print(f"Congrats, {current_player}! You've won!")
            break
        elif board_is_full(board):
            print("Cat's game! No winners.")
            break

        current_player = change_player(current_player, p1_name, p2_name)


if __name__ == "main":
    main()


