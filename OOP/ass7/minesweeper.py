from board import Board
import tkinter as tk


class Minesweeper:
    def __init__(self, root: tk.Tk, size: int, bomb_count: int):
        self.board = Board(root, size, bomb_count)
        self.size = size
        self.bomb_count = bomb_count
        self.r = root

        self.construct_tkinter()

    def construct_tkinter(self):
        self.r.title("Minesweeper") 
        
        board_frame = self.board.construct_tkinter()
        board_frame.pack(expand=True, side=tk.TOP, fill=tk.BOTH)
        

