import numpy as np
from config import Config

DIFF = -1
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

    def calculate_result(self, matrix, direction_matrix, seq_a, seq_b, file_path):
        f = open(file_path, 'w')
        flag = True
        score = matrix[len(seq_a)][len(seq_b)]
        f.write('SCORE=' + str(score) + '\n')
        f.write('\n')
        while(flag):
            flag = False
            row = len(seq_a)
            col = len(seq_b)
            res_a = ""
            res_b = ""
            current_direction = direction_matrix[row][col]
            p_x = 0
            p_y = 0
            while (current_direction is not None) and (row > 0) and (col > 0):
                if len(current_direction) > 1:
                    p_x = row
                    p_y = col
                    flag = True
                    current_direction = current_direction[len(current_direction)-1]
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
                    col = col -1
                current_direction = direction_matrix[row][col]
            f.write(res_a + '\n')
            f.write(res_b + '\n')
            f.write('\n')
            if flag:
                direction_matrix[p_x][p_y] = direction_matrix[p_x][p_y][:-1]
        f.close()


