#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    first_list = []
    second_list = []
    third_list = []
    n = len(matrix)
    if n == 0:
        return matrix
    if n == 1:
        for i in range(len(matrix[0])):
            first_list.append(int(matrix[0][i] ** 2))

        new_list.extend([first_list])
        return new_list
    if n == 2:
        for i in range(len(matrix[0])):
            first_list.append(int(matrix[0][i] ** 2))
        for j in range(len(matrix[1])):
            second_list.append(int(matrix[1][j] ** 2))

        new_list.extend([first_list, second_list])
        return new_list
    if n == 3:
        for i in range(len(matrix[0])):
            first_list.append(int(matrix[0][i] ** 2))
        for j in range(len(matrix[1])):
            second_list.append(int(matrix[1][j] ** 2))
        for k in range(len(matrix[2])):
            third_list.append(int(matrix[2][k] ** 2))

        new_list.extend([first_list, second_list, third_list])
        return new_list

        # new_list = []
        # first_list = []
        # second_list = []
        # third_list = []
        # for i in range(len(matrix[0])):
        #     first_list.append(int(matrix[0][i] ** 2))
        # for j in range(len(matrix[1])):
        #     second_list.append(int(matrix[1][j] ** 2))
        # for k in range(len(matrix[2])):
        #     third_list.append(int(matrix[2][k] ** 2))

        # new_list.extend([first_list, second_list, third_list])
        # return new_list
