from random import sample
import tkinter as tk
import tkinter.messagebox as messagebox

from cell import Cell


class Board:
    DIFFKERNEL = [-1, 0, 1]

    def __init__(self, root, size, mine_count):
        self.r = root

        self.tk_frame = tk.Frame(self.r)
        for r in range(size):
            self.tk_frame.grid_rowconfigure(r, weight=1, uniform="row")
        for c in range(size):
            self.tk_frame.grid_columnconfigure(c, weight=1, uniform="col")

        self.size = size
        self.board = [
            [
                Cell(
                    self.tk_frame,
                    x,
                    y,
                    lambda x=x, y=y: self.cell_lclck_callback(x, y),
                    lambda _, x=x, y=y: self.cell_rclck_callback(x, y),
                )
                for y in range(size)
            ]
            for x in range(size)
        ]

        self.mine_count = mine_count

        positions = [(i, j) for i in range(size) for j in range(size)]
        self.mine_positions = sample(positions, mine_count)
        for pos_x, pos_y in self.mine_positions:
            self.board[pos_x][pos_y].val = -1

        for x in range(size):
            for y in range(size):
                cell = self.board[x][y]
                if cell.val != -1:
                    cell.val = self.neighbour_mine_count(cell)

    def neighbour_mine_count(self, cell):
        count = 0
        for neighbour in self.neighbours(cell):
            count += neighbour.val == -1
        return count

    def neighbours(self, cell):
        neighbours = []
        for dx in self.DIFFKERNEL:
            for dy in self.DIFFKERNEL:
                cx, cy = cell.x + dx, cell.y + dy
                if cx < 0 or cy < 0 or cx >= self.size or cy >= self.size:
                    continue

                neighbour = self.board[cx][cy]
                neighbours.append(neighbour)

        return neighbours

    def reveal_recursive(self, start):
        queue = [start]
        visited = []
        while len(queue):
            cell = queue.pop(0)
            cell.reveal()
            visited.append(cell)

            if cell.val == 0:
                neighbours = self.neighbours(cell)
                for n in neighbours:
                    if n not in visited and n not in queue:
                        queue.append(n)

    def reveal_all(self):
        for x in range(self.size):
            for y in range(self.size):
                self.board[x][y].reveal()
         

    def cell_lclck_callback(self, x: int, y: int):
        cell = self.board[x][y]
        if cell.val == -1:
            self.reveal_all()
            messagebox.showinfo("Game Over", "You hit a mine!")
            exit(0)
        else:
            self.reveal_recursive(cell)

    def cell_rclck_callback(self, x: int, y: int):
        self.board[x][y].mark()
        self.check_win()

    def check_win(self):
        correct = 0
        for x in range(self.size):
            for y in range(self.size):
                cell = self.board[x][y]
                if cell.state == cell.possible_states["flagged"] and cell.val == -1:
                    correct += 1

                    if correct == self.mine_count:
                        self.reveal_all()
                        messagebox.showinfo("Game over", "Congratulations! You cleared the board")
                        exit(0)

    def construct_tkinter(self):
        for x in range(self.size):
            for y in range(self.size):
                cell_display = self.board[x][y].tk
                cell_display.grid(row=x, column=y, sticky="nsew")
                

        return self.tk_frame
