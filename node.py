class Node:
    seq_a: str
    seq_b: str
    co_x: int
    co_y: int
    current_direction: str

    def __init__(self, seq_a, seq_b, co_x, co_y, current_direction):
        self.seq_a = seq_a
        self.seq_b = seq_b
        self.co_x = co_x
        self.co_y = co_y
        self.current_direction = current_direction