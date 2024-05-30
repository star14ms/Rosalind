from util import get_data, get_output_path
import numpy as np


def is_consistent(matrix):
    num_cols = len(matrix[0])
    num_rows = len(matrix)
    
    # column_kinds = {}
    # for i in range(num_cols):
    #     if column_kinds.get(tuple(matrix[:,i]), None) is not None:
    #         column_kinds[tuple(matrix[:,i])] += 1
    #     else:
    #         column_kinds[tuple(matrix[:,i])] = 1
    
    # row_kinds = {}
    # for i in range(num_rows):
    #     if row_kinds.get(tuple(matrix[i]), None) is not None:
    #         row_kinds[tuple(matrix[i])] += 1
    #     else:
    #         row_kinds[tuple(matrix[i])] = 1
            
    # if len(column_kinds) > len(matrix) or len(row_kinds) > len(matrix[0]):
    #     return False

    print(num_rows, end='\r')
    if num_rows == 2:
        return True
    
    row_sum = np.sum(matrix, axis=0)

    if row_sum:
        return True

    max_n_1 = max(row_sum)
    min_n_1 = min(row_sum)

    for i in np.where(row_sum == max_n_1)[0].tolist() + np.where(row_sum == min_n_1)[0].tolist():
        matrix_deleted = np.delete(matrix, i, axis=0)
        left = np.zeros_like(matrix[:-1,:1])
        right = np.zeros_like(matrix[:-1,:1])

        for j in range(num_cols):
            if matrix[i][j] == 1:
                left = np.concatenate((left, matrix_deleted[:,j:j+1]), axis=1) 
            else:
                right = np.concatenate((right, matrix_deleted[:,j:j+1]), axis=1) 

        if is_consistent(left[:,1:]) and is_consistent(right[:,1:]):
            # print(left[:,1:])
            # print(right[:,1:])
            return True
        
    return False


# def is_consistent(matrix):
#     num_cols = len(matrix[0])
#     num_rows = len(matrix)
    
#     column_kinds = {}
#     for i in range(num_cols):
#         if column_kinds.get(tuple(matrix[:,i]), None) is not None:
#             column_kinds[tuple(matrix[:,i])] += 1
#         else:
#             column_kinds[tuple(matrix[:,i])] = 1
    
#     row_kinds = {}
#     for i in range(num_rows):
#         if row_kinds.get(tuple(matrix[i]), None) is not None:
#             row_kinds[tuple(matrix[i])] += 1
#         else:
#             row_kinds[tuple(matrix[i])] = 1
            
#     if len(column_kinds) > len(matrix) or len(row_kinds) > len(matrix[0]):
#         # print(num_rows, end='\r')
#         return False

#     # print(len(column_kinds), len(matrix))
#     # print(len(row_kinds), len(matrix[0]))
#     # breakpoint()

#     print(num_rows, end='\r')
#     if num_rows == 2:
#         return True
#         # print(matrix)
#         # print((np.sum(matrix, axis=0) == 1).all())
#         # print(not np.any(matrix != matrix[0][0]))
#         # print((matrix[0] == matrix[1]).all())
#         # breakpoint()
#         # if (np.sum(matrix, axis=0) == 1).all() or not np.any(matrix != matrix[0][0]) or (matrix[0] == matrix[1]).all():
#         #     return True
#         # else:
#         #     return False

#     for i in range(num_rows):
#         matrix_deleted = np.delete(matrix, i, axis=0)
        
#         splited_cols1 = np.zeros_like(matrix[:-1,:1])
#         splited_cols2 = np.zeros_like(matrix[:-1,:1])

#         for j in range(num_cols):
#             if matrix[i][j] == 1:
#               splited_cols1 = np.concatenate((splited_cols1, matrix_deleted[:,j:j+1]), axis=1) 
#             else:
#               splited_cols2 = np.concatenate((splited_cols2, matrix_deleted[:,j:j+1]), axis=1) 

#         if is_consistent(splited_cols1[:,1:]) and is_consistent(splited_cols2[:,1:]):
#             # print(splited_cols1[:,1:])
#             # print(splited_cols2[:,1:])
#             return True
        
#     return False


def find_consistent_submatrix(matrix):
    for row_index in range(len(matrix)):
        # Create a new matrix without the current row
        new_matrix = np.delete(matrix, row_index, axis=0)
        
        if is_consistent(new_matrix):
            return new_matrix

    return None  # In case no consistent submatrix is found


if __name__ == '__main__':
    data = get_data(__file__)
#     data = '''100001
# 000110
# 111000
# 100111'''

    # Convert strings to lists of integers
    C = np.array([[int(char) for char in row] for row in data.strip().split('\n')])
    print(C.shape)
    
    # Find a consistent submatrix
    result = find_consistent_submatrix(C)

    # Convert result back to the required format if a result is found
    if result is not None:
        result = [''.join(map(str, row)) for row in result]

        # Print output
        with open(get_output_path(__file__), 'w') as f:
            for line in result:
                f.write(line + '\n')
                print(line)
    else:
        print("No consistent submatrix found")
        
    