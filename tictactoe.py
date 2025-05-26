import random
global board
board = [[1, 2, 3],\
        [4, 5, 6],\
        [7, 8, 9]]
line = "-" * 25
space = "|" + (' ' * 7 +  '|') * 3


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    #print("\33c", end="")
    print(line)
    for row in board:
        print(space)
        fill = '|' + ''.join(f"   {x}   |" for x in row)
        print(f"{space}\n{fill}\n{space}\n{line}\n")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    global sign
    user_input = int(input("Number: "))
    sign = "O"
    if user_input / 3 <= 1:
        x = 0
    elif user_input / 3 <= 2:
        x = 1
    elif user_input / 3 <= 3:
        x = 2

    y = board[x].index(user_input)
    board[x][y] = sign
    display_board(board)
    return board[x][y] and sign

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_fields
    free_fields = []
    for i in range(1,10):
        if i / 3 <= 1:
            x = 0
        elif i / 3 <= 2:
            x = 1
        elif i / 3 <= 3:
            x = 2
        try:
            y = board[x].index(i)
        except:
            continue
        free_fields.append((x, y))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    print (f"checking if {sign} has won: ...")
    for x in range(3):
        if iter in board == [sign, sign, sign]:
            print(f"{sign} WINS!")
            main() 
        elif board[0][x] == sign and board[1][x] == sign and board[2][x] == sign:
            print(f"{sign} WINS!")
            main()
        elif board[x][0] == sign and board[x][1] == sign and board[x][2] == sign:
            print(f"{sign} WINS!")
            main()    
        elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            print(f"{sign} WINS!")
            main()
        elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            print(f"{sign} WINS!")
            main()
        else: continue

def draw_move(board):

    # The function draws the computer's move and updates the board.
    make_list_of_free_fields(board)
    sign = "X"
    x, y = random.choice(free_fields)
    board[x][y] = sign
    display_board(board)
    return board[x][y] and sign

def main():
    board = [[1, 2, 3],\
            [4, 5, 6],\
            [7, 8, 9]]
    print("NEW GAME")
    display_board(board)
    print("\n\n\n")
    draw_move(board)
    print("\n\n\n")
    enter_move(board)
    print("\n\n\n")
    draw_move(board)
    print("\n\n\n")
    enter_move(board)
    print("\n\n\n")
    draw_move(board)
    print("\n\n\n")
    victory_for(board, "X")
    print("\n\n\n")
    enter_move(board)
    print("\n\n\n")
    victory_for(board, "O")
    print("\n\n\n")
    draw_move(board)
    print("\n\n\n")
    victory_for(board, "X")
    print("\n\n\n")
    enter_move(board)
    print("\n\n\n")
    victory_for(board, "O")
    print("\n\n\n")
    draw_move(board)
    print("\n\n\n")
    victory_for(board, "X")
    print("\n\n\n")
    print("IT WAS A DRAW!!")
main()