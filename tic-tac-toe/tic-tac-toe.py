import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = ""
        self.buttons = []
        self.game_active = False

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, width=10, height=5, command=lambda i=i, j=j: self.button_clicked(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
            self.choose_player("X")

    def choose_player(self, player):
        self.current_player = player
        self.game_active = True

    def button_clicked(self, i, j):
        if not self.buttons[i][j]["text"] and self.game_active:
            self.buttons[i][j].config(text=self.current_player)
        if self.check_winner():
            messagebox.showinfo("Game Over", f"Player {self.current_player} Wins!\nClick OK to reset the game.")
            self.reset_game()
            return
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!\nClick OK to reset the game.")
            self.reset_game()
            return
        # Switch players
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
        for j in range(3):
            if  self.buttons[0][j]["text"] == self.buttons[1][j]["text"] == self.buttons[2][j]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True

        return False
    
    def is_draw(self):
        return all(self.buttons[i][j]["text"] for i in range(3) for j in range(3))
    
    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = ""
        self.choose_player("X")
        self.game_active = True
        
if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()
