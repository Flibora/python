# Создать lambda функцию, которая принимает на вход
# неопределенное количество именных аргументов и
# выводит словарь с ключами удвоенно длины. {‘abc’:
# 5} -> {‘abcabc’: 5}


def main():
    dict = ['dsfs': 3, 'fdg2r': 34, 'erqwe': 432]
    print(map((lambda **x: {k*2: v for k, v in x.items()})(dict)))
    # print((lambda **x: {k*2: v for k, v in x.items()})



if __name__ == "__main__":
    main()
