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

        self.turn_label = tk.Label(self.root, text="Choose your player: X or O")
        self.turn_label.grid(row=3, column=0, columnspan=3)

        self.player_x_button = tk.Button(self.root, text="Player X", command=lambda: self.choose_player("X"))
        self.player_x_button.grid(row=4, column=0)

        self.player_o_button = tk.Button(self.root, text="Player O", command=lambda: self.choose_player("O"))
        self.player_o_button.grid(row=4, column=1)

        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=4, column=2)

    def choose_player(self, player):
        self.current_player = player
        self.turn_label.config(text=f"Player {self.current_player}'s turn")
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
        self.toggle_player()

            
        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label.config(text=f"Player {self.current_player}'s turn")

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
        self.turn_label.config(text=f"Player {self.current_player}'s turn")

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = ""
        self.turn_label.config(text="Choose your player: X or O")
        self.game_active = False
        

if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()
