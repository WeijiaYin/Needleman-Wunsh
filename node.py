class Node:
    # store the paths
    seq_a: str
    seq_b: str
    co_x: int
    co_y: int
    current_direction: str

    def __init__(self, seq_a, seq_b, co_x, co_y, current_direction):
        """

        :param seq_a: current sequence a
        :param seq_b: current sequence b
        :param co_x: current position x
        :param co_y: current position y
        :param current_direction: current direction
        """
        self.seq_a = seq_a
        self.seq_b = seq_b
        self.co_x = co_x
        self.co_y = co_y
        self.current_direction = current_direction
