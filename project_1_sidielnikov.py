board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]] # Computer is "X", player is "O". Computer made the first move.

game_over = False

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    clear_screen()
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[0][0]) + "   |   " + str(board[0][1]) + "   |   " + str(board[0][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[1][0]) + "   |   " + str(board[1][1]) + "   |   " + str(board[1][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[2][0]) + "   |   " + str(board[2][1]) + "   |   " + str(board[2][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    global game_over
    if game_over == True:
        return
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    try:
        move = int(input("Enter your move: "))
        
        if move < 1 or move > 9:
            raise ValueError
    except ValueError:
        print("Invalid move, try again!")
        enter_move(board)
        return
    
    move -= 1

    x = move // 3
    y = move % 3

    free_fields = make_list_of_free_fields(board)

    if (x, y) not in free_fields:
        print("Invalid move, try again!")
        enter_move(board)
        return
    
    board[x][y] = "O"
    game_over = victory_for(board, "O")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for x in range(3):
        for y in range(3):
            if board[x][y] != "X" and board[x][y] != "O":
                free_fields.append((x, y))
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    
    return False


def draw_move(board):
    # The function makes the move for the computer and updates the board.
    global game_over
    if game_over == True:
        return
    
    import random
    free_fields = make_list_of_free_fields(board)
    move = random.choice(free_fields)
    board[move[0]][move[1]] = "X"
    game_over = victory_for(board, "X")

def clear_screen():
    print("\033[H\033[J", end="")

display_board(board)
while game_over == False:
    enter_move(board)

    display_board(board)

    if game_over:
        break
    elif make_list_of_free_fields(board) == []:
        break
    draw_move(board)

    display_board(board)
    
    if game_over:
        break
    elif make_list_of_free_fields(board) == []:
        break

if victory_for(board, "O"):
    print("You won!")
elif victory_for(board, "X"):
    print("Computer won!")
else:
    print ("Draw!")
print("\nGame over!")