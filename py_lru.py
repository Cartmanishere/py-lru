class Node:
    def __init__(self, value, k=None):
        self.val = value
        self.left = None
        self.right = None
        self.key = k

    def __repr__(self):
        return f'({self.key + ":" if self.key else ""}{self.val})'



