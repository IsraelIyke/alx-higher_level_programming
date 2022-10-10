#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    first_list = []
    second_list = []
    third_list = []
    for i in range(len(matrix[0])):
        first_list.append(int(matrix[0][i] ** 2))
    for j in range(len(matrix[1])):
        second_list.append(int(matrix[1][j] ** 2))
    for k in range(len(matrix[2])):
        third_list.append(int(matrix[2][k] ** 2))

    new_list.extend([first_list, second_list, third_list])
    return new_list
