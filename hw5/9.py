# Для каждого натурального числа в промежутке от m до
# n вывести все делители, кроме единицы и самого
# числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35

n = int(input())
m = int(input())

for num in range(n, m + 1):
    spisok_del = [x for x in range(1, num//2 + 1) if num % x == 0]
    #доюавляет значение х в список, если делении num на х без остатка в
    #промежутке от 1 до половины num
    spisok_del.remove(1)
    print(f"{num} : {spisok_del}")
