import math
game_board = [' ' for i in range(9)]
hi='X'
ai='O'
def print_board(game_board):
    for i in range(0,9,3):
        print("|".join(game_board[i:i+3]))

def get_empty_cells(game_board):
    return [i for i, cell in enumerate(game_board) if cell == ' ']

def is_winner(game_board,player):
    winning_combinations=[
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]]
    return any(all(game_board[i] == player for i in combo) for combo in winning_combinations)

def is_board_full(game_board):
    return ' ' not in game_board

def evaluate(game_board):
    if is_winner(game_board,ai):
        return 1
    elif is_winner(game_board,hi):
        return -1
    else:
        return 0    

def minimax(game_board,depth,alpha,beta,maximizing_player):
    if depth==0 or is_winner(game_board,hi) or is_winner(game_board,ai) or is_board_full(game_board):
        return evaluate(game_board)

    if maximizing_player:
        max_val=-math.inf
        for cell in get_empty_cells(game_board):
            game_board[cell]=ai
            val=minimax(game_board,depth-1,alpha,beta,False)
            game_board[cell]=' '
            max_val=max(max_val, val)
            alpha=max(alpha, max_val)
            if beta<=alpha:
                break
        return max_val
    else:
        min_val=math.inf
        for cell in get_empty_cells(game_board):
            game_board[cell]=hi
            val=minimax(game_board,depth-1,alpha,beta,True)
            game_board[cell] = ' '
            min_val=min(min_val,val)
            beta = min(beta,min_val)
            if beta<=alpha:
                break
        return min_val

def find_best_move(game_board):
    best_val=-math.inf
    best_move=-1
    alpha=-math.inf
    beta=math.inf
    for cell in get_empty_cells(game_board):
        game_board[cell]=ai
        val=minimax(game_board,9,alpha,beta,False)
        game_board[cell]=' '
        if val>best_val:
            best_val=val
            best_move=cell
        alpha=max(alpha,best_val)
    return best_move
    
def play_game():
    print("Who will play the First Move(select):1.ME   2.AI")
    op=int(input("Enter the option:"))
    if(op==1):
        current_player=hi
    else:
        current_player=ai
    while not is_winner(game_board,hi) and not is_winner(game_board,ai) and not is_board_full(game_board):
        if current_player == hi:
            print("Your turn (", hi, ")")
            move=int(input("Enter your move (1-9):"))
            move-=1
            if move not in get_empty_cells(game_board):
                print("Invalid move,Try again.....")
                continue
        else:
            print("AI's turn (", ai, ")")
            move=find_best_move(game_board)
        game_board[move]=current_player
        print_board(game_board)
        current_player=hi if current_player == ai else ai
    if is_winner(game_board,hi):
        print("You win the Game.....!")
    elif is_winner(game_board,ai):
        print("AI wins!.....")
    else:
        print("It's a draw!.....")

print(".....Tic Tac Toe!.....")
print("Initial board:")
print_board(game_board)
play_game()
