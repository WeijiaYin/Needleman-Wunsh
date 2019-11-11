import numpy as np
from config import Config
from node import Node
from alignment import Alignment

LEFT = "L"
UP = "U"
DIAGONAL = "D"


class NeedlemanWunsh:

    def calculate_diagonal(self, a,b, config = Config):
        if a == b:
            return config.SAME
        if a != b:
            return config.DIFF

    def calculate_matrix(self, seq_a, seq_b, config = Config):
        seq_a = "_" + seq_a
        seq_b = "_" + seq_b

        matrix = np.zeros(shape=(len(seq_a), len(seq_b)), dtype=int)
        direction_matrix = np.empty(shape=(len(seq_a), len(seq_b)), dtype=object)

        for i in range(len(seq_a)):
            for j in range(len(seq_b)):
                if i == 0 and j == 0:
                    matrix[i][j] = 0
                    direction_matrix[i][j] = None
                elif i == 0 and j != 0:
                    matrix[i][j] = j * config.GAP_PENALTY
                    direction_matrix[i][j] = LEFT
                elif j == 0 and i != 0:
                    matrix[i][j] = i * config.GAP_PENALTY
                    direction_matrix[i][j] = UP
                else:
                    diagonal = matrix[i-1][j-1] + self.calculate_diagonal(seq_a[i], seq_b[j], config)
                    left = matrix[i][j-1] + config.GAP_PENALTY
                    up = matrix[i-1][j] + config.GAP_PENALTY
                    max_value = max(diagonal, left, up)
                    matrix[i][j] = max_value
                    value = ''
                    if(max_value == up):
                        value = value + UP
                    if(max_value == left):
                        value = value + LEFT
                    if(max_value == diagonal):
                        value = value + DIAGONAL
                    direction_matrix [i][j] = value
        return matrix, direction_matrix

    def calculate_result(self, matrix, direction_matrix, seq_a, seq_b, config = Config):
        score = matrix[len(seq_a)][len(seq_b)]

        n = Node('', '', len(seq_a), len(seq_b), direction_matrix[len(seq_a)][len(seq_b)])
        l = []
        l.append(n)
        res = []

        while len(l):
            flag = True
            row = l[0].co_x
            col = l[0].co_y
            res_a = l[0].seq_a
            res_b = l[0].seq_b
            current_direction = l[0].current_direction
            while (current_direction is not None) and (row > 0) and (col > 0):
                if len(current_direction) > 1:
                    l.remove(l[0])
                    for i in range(len(current_direction)):
                        m = Node(res_a, res_b, row, col, current_direction[i])
                        l.append(m)
                    flag = False
                    break
                if current_direction == LEFT:
                    res_a = "_" + res_a
                    res_b = seq_b[col - 1] + res_b
                    col = col - 1
                elif current_direction == UP:
                    res_a = seq_a[row - 1] + res_a
                    res_b = "_" + res_b
                    row = row - 1
                elif current_direction == DIAGONAL:
                    res_a = seq_a[row - 1] + res_a
                    res_b = seq_b[col - 1] + res_b
                    row = row - 1
                    col = col - 1
                current_direction = direction_matrix[row][col]
            if flag:
                al = Alignment(res_a, res_b)
                res.append(al)
                l.remove(l[0])
                if len(res) == config.MAX_NUMBER_PATH:
                    break
        return score, res

