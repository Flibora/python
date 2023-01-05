# Создать декоратор для функции, которая принимает
# список чисел. Декоратор должен производить
# предварительную проверку данных - удалять все
# четные элементы из списка.

import random

def decor_func(func):
    elem = func()
    print(elem)
    def elem_check(elem):
        return list(filter(lambda x: x % 2, elem))
    return elem_check(elem)



def main():

    @decor_func
    def list_elements():
        return [random.randint(0, 100) for x in range(0, 20)]

    result = list_elements
    print(result)

if __name__ == "__main__":
    main()
