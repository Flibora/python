# Создать две новые матрицы matrix_a, matrix_b
# случайных чисел размерностью n*m;
# a. создать матрицу равную сумме matrix_a и matrix_b;
# b.создать матрицу равную разности matrix_a и
# matrix_b;
# c. создать новую матрицу равную matrix_a умноженно
# на число g. g вводится с клавиатуры.

import random

matrix_a = []
matrix_b = []

n = int(input())
m = int(input())
for i in range(n):
    line_a = []
    line_b = []
    for j in range(m):
        line_a.append(random.randint(0 , 99))
        line_b.append(random.randint(0 , 99))
    matrix_a.append(line_a)
    matrix_b.append(line_b)

for line in matrix_a:
    print(line)
print()

for line in matrix_b:
    print(line)
print()

new_matrix_summa = []
new_matrix_razn = []
new_matrix_multiply = []

print('введите множитель g -' )
g = int(input())

for i in range(n):
    new_line_summa = []
    new_line_razn = []
    new_line_multiply = []
    for j in range(m):
        new_line_summa.append(matrix_a[i][j] + matrix_b[i][j])
        new_line_razn.append(matrix_a[i][j] - matrix_b[i][j])
        new_line_multiply.append(matrix_a[i][j] * g)
    new_matrix_summa.append(new_line_summa)
    new_matrix_razn.append(new_line_razn)
    new_matrix_multiply.append(new_line_multiply)

for line in new_matrix_summa:
    print(line)
print()

for line in new_matrix_razn:
    print(line)
print()

for line in new_matrix_multiply:
    print(line)
print()
