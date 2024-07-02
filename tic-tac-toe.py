import tkinter as tk
from tkinter import messagebox
import random


PLAYER = 'X'
COMPUTER = 'O'


def initialize_game():
    global current_player, board
    current_player = PLAYER
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state=tk.NORMAL)


def check_win(player, board):
   
    for row in board:
        if all([cell == player for cell in row]):
            return True
  
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def minimax(board, depth, is_maximizing):
    if check_win(PLAYER, board):
        return -10 + depth
    elif check_win(COMPUTER, board):
        return 10 - depth
    elif is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = COMPUTER
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score


def get_best_move(board):
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = COMPUTER
                score = minimax(board, 0, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


def on_button_click(row, col):
    global current_player, board
    
    if board[row][col] == ' ':
        buttons[row][col].config(text=PLAYER, state=tk.DISABLED)
        board[row][col] = PLAYER
        
        # Check for win or tie
        if check_win(PLAYER, board):
            messagebox.showinfo("Tic Tac Toe", "You win!")
            initialize_game()
            return
        elif is_board_full(board):
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            initialize_game()
            return
        
        row, col = get_best_move(board)
        buttons[row][col].config(text=COMPUTER, state=tk.DISABLED)
        board[row][col] = COMPUTER
        
     
        if check_win(COMPUTER, board):
            messagebox.showinfo("Tic Tac Toe", "Computer wins!")
            initialize_game()
        elif is_board_full(board):
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            initialize_game()


root = tk.Tk()
root.title("Tic Tac Toe")


buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('Helvetica', 20), width=6, height=3,
                                  command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)


initialize_game()


root.mainloop()
