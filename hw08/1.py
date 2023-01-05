# Создать декоратор для функции, которая принимает
# список чисел. Декоратор должен производить
# предварительную проверку данных - удалять все
# четные элементы из списка.

from functools import reduce

def decor_func(function_to_decorate):
    def elem_check(arg):
        new_arg = filter(lambda x: x % 2, arg)
        return function_to_decorate(new_arg)
    return elem_check

def main():

    @decor_func
    def list_elements(list_el):
        return reduce(lambda x,n: x*n, list_el)

    @decor_func
    def list_elem(list_el):
        return reduce(lambda x,n: x+n, list_el)

    print(list_elements([1,2,3,4,5,6]))
    print(list_elem([1,2,3,4,5,6]))


if __name__ == "__main__":
    main()
