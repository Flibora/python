# Дана целочисленная квадратная матрица размерности
# n. Заполнить ее случайными целыми числами. На ти в
# каждо строке наибольши элемент и поменять его
# местами с элементом главно диагонали.

matrix = []

n = int(input())

for i in range(n):
    line = []
    for j in range(n):
        line.append(int(input()))
    matrix.append(line)

print(matrix)

for k in range(n):
    for i in range(n):
        if matrix[k][i] == max(matrix[k]):
            matrix[k][k], matrix[k][i] = matrix[k][i], matrix[k][k]

print(matrix)



#########################################################
