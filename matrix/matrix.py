# 1. Создать матрицу случа ных чисел от a до b,
# размерность матрицы n*m;
# a. на ти максимальны элемент матрицы;
# b. на ти минимальны минимальны матрицы;
# c. на ти сумму всех элементов матрицы;
# d. на ти индекс ряда с максимально суммо
# элементов;
# e. на ти индекс колонки с максимально суммо
# элементов;
# f.
# на ти индекс ряда с минимально суммо
# элементов;
# g. на ти индекс колонки с минимально суммо
# элементов;
# h. обнулить все элементы выше главно диагонали;
# i.
# обнулить все элементы ниже главно диагонали.
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

max_element = line[0]
min_element = line[0]
summa = 0
index_max_line = 0
index_min_line = 0
summa_collun = list(range(n))
index_max_collun = 0
index_min_collun = 0

for i, line in enumerate(matrix):
    summa_line = 0
    for j, elem in enumerate(line):
        summa += elem
        summa_line += elem
        summa_collun[j]+=line[j]
        if max_element < elem:
            max_element = elem
        elif min_element > elem:
            min_element = elem
        if summa_line < summa:
            index_max_line = j
        elif summa_line > summa:
            index_min_line = j
        if j > 0:
            elem = 0

for i, elem in enumerate(summa_collun):
    if elem == max(summa_collun):
        index_max_collun = i
    elif elem == min(summa_collun):
        index_min_collun = i

print(f'максимальынй элемент - {max_element}')
print(f'минимальный элемент - {min_element}')
print(f'сумма - {summa}')
print(f'индекс ряда с максимальной суммой - {index_max_line}')
print(f'индекс минимального ряда - {index_min_line}')
print(f'индекс максимальной колонки - {index_max_collun}')
print(f'индекс минимальной колонки - {index_min_collun}')

for i, line in enumerate(matrix):
    for j, elem in enumerate(matrix):
        if j > i:
            matrix[i][j] = 0

for line in matrix:
    print(line)
print()

for i, line in enumerate(matrix):
    for j, elem in enumerate(matrix):
        if j < i:
            matrix[i][j] = 0

for line in matrix:
    print(line)
print()
