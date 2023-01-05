# Создать декоратор для функции, которая принимает
# список чисел. Декоратор должен производить
# предварительную проверку данных - удалять все
# четные элементы из списка.

# import random
#
# def decor_func(func):
#     elem = func()
#     print(elem)
#     def elem_check(elem):
#         return list(filter(lambda x: x % 2, elem))
#     return elem_check(elem)
#
#
#
# def main():
#
#     @decor_func
#     def list_elements():
#         return [random.randint(0, 100) for x in range(0, 20)]
#
#     result = list_elements
#     print(result)
#
# if __name__ == "__main__":
#     main()

import random

def decor_func(func):
    def elem_check(elem):
        return list(filter(lambda x: x % 2, elem))
    return elem_check

def main():

    @decor_func
    def list_elements(list):
        Pass

    list_elem = [1,3,4,5,2,34,4,65,67,2,31,243,5,46,23,1,232,1,454,562,2,3]
    print(list_elements(list_elem))

if __name__ == "__main__":
    main()
