# 1. Напишите функцию для транспонирования матрицы

def print_matrix(matrix: [[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f'{matrix[i][j]:>3}', end=" ")
        print()
    print()


def transposed_matrix(matrix: [[int]]) -> [[int]]:
    transposet_matrix = [[0] * len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(transposet_matrix)):
        for j in range(len(transposet_matrix[0])):
            transposet_matrix[i][j] = matrix[j][i]
    return transposet_matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print_matrix(matrix)
print_matrix(transposed_matrix((matrix)))
