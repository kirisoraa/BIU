import tkinter as tk
from minesweeper import Minesweeper

if __name__ == "__main__":
    s = int(input("Enter the size of the board: "))
    b = int(input("Enter the number of bombs: "))
    root = tk.Tk()
    game = Minesweeper(root, size=s, bomb_count=b)
    root.mainloop()
