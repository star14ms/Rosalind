from util import get_data
import numpy as np


""" Find the Length of a Longest Path in a Manhattan-like Grid """

def read_data(file_name):
    with open(file_name, 'r+') as file:
        line = file.readline().split()
        n = int(line[0].strip())
        m = int(line[1].strip())
        down_matrix = [[0]*(m+1) for _ in range(n)]
        for i in range(n):
            line = [int(item.strip()) for item in file.readline().split()]
            for j in range(m+1):
                down_matrix[i][j] = line[j]

        file.readline()
        right_matrix = [[0]*(m) for _ in range(n+1)]
        for i in range(n+1):
            line = [int(item.strip()) for item in file.readline().split()]
            for j in range(m):
                right_matrix[i][j] = line[j]

        return n, m, down_matrix, right_matrix

def longest_manh_path(n, m, down, right):
    score = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        score[i][0] = score[i - 1][0] + down[i - 1][0]

    for j in range(1, m+1):
        score[0][j] = score[0][j - 1] + right[0][j - 1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            score[i][j] = max(score[i - 1][j] + down[i - 1][j], score[i][j - 1] + right[i][j - 1])

    return score[n][m]

if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''4 4
# 1 0 2 4 3
# 4 6 5 2 1
# 4 4 5 2 1
# 5 6 8 5 3
# -
# 3 2 4 0
# 3 2 4 2
# 0 7 3 3
# 3 3 0 2
# 1 3 2 2'''

    integers, matrices = data.split('\n', 1)
    m, n = map(int, integers.split())
    matrix_down, matrix_right = matrices.split('\n-\n')

    matrix_down = np.array([list(map(int, row.split())) for row in matrix_down.split('\n')])
    matrix_right = np.array([list(map(int, row.split())) for row in matrix_right.split('\n')])
    
    print(matrix_down)
    print(matrix_right)

    length_longest_path = longest_manh_path(m, n, matrix_down, matrix_right)

    print(length_longest_path)    
