# Создать универсальны декоратор, которы меняет
# порядок аргументов в функции на противоположны .


def decor_universal(func):
    def new_func(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return new_func

def main():

    @decor_universal
    def func(a, b, c):
        return a * b  - c

    def funci(a, b, c):
        return a * b  - c

    x = 11
    y = 12
    z = 13

    print(funci(x, y, z))
    print(func(x, y ,z))



if __name__ == "__main__":
    main()
