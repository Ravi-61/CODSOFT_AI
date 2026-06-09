import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("--+---+--")
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True

    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score

def best_move():

    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

while True:

    print_board()

    try:
        human_move = int(input("Enter your move (1-9): ")) - 1

        if human_move < 0 or human_move > 8:
            print("Invalid position!")
            continue

        if board[human_move] != " ":
            print("Position already taken!")
            continue

    except ValueError:
        print("Please enter a number between 1 and 9.")
        continue

    board[human_move] = "X"

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("🤝 Draw!")
        break

    ai_move = best_move()
    board[ai_move] = "O"

    print(f"🤖 AI chooses position {ai_move + 1}")

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if is_draw():
        print_board()
        print("🤝 Draw!")
        break