import tkinter as tk


class Cell:
    possible_states = {
            "hidden": 0,
            "revealed": 1,
            "flagged": 2
            }
    def __init__(self, root, x, y, lclck_callback, rclck_callback):
        self.r = root
        self.x = x
        self.y = y
        self.tk = tk.Button(
            self.r,
            command=lclck_callback,
        )
        self.tk.bind(
            "<Button-3>", rclck_callback
        )
        self.val = 0
        self.state = self.possible_states["hidden"]

    def reveal(self):
        self.state = self.possible_states["revealed"]
        if self.val == 0:
            self.tk.config(text = "", state = "disabled", bg="white")
        elif self.val == -1:
            self.tk.config(text = "X", state = "disabled", bg="red")
        else:
            self.tk.config(text = str(self.val), state = "disabled", bg="white")

    def mark(self):
        if self.state == self.possible_states["hidden"]:
            self.state = self.possible_states["flagged"]
            self.tk.config(text = "X", bg="yellow")
        elif self.state == self.possible_states["flagged"]:
            self.state = self.possible_states["hidden"]
            self.tk.config(text = "", bg="gray")
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return f"Cell ({self.x}, {self.y}) = {self.val}"

    def __repr__(self):
        return self.__str__()

