# Дана целочисленная квадратная матрица размерности
# n. Заполнить ее случайными целыми числами. На ти в
# каждо строке наибольши элемент и поменять его
# местами с элементом главно диагонали.
import random

matrix = []

n = int(input())

for i in range(n):
    line = []
    for j in range(n):
        line.append(random.randint(0 , 99))
    matrix.append(line)

for line in matrix:
    print(line)
print()

for i, line in enumerate(matrix):
        max_element = line[0]
        max_index = 0
        for j, elem in enumerate(line):
            if max_element < elem:
                max_element = elem
                max_index = j
        matrix[i][max_index], matrix[i][i] = matrix[i][i], max_element


for line in matrix:
    print(line)
print()
