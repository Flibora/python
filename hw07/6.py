# Создать lambda функцию, которая принимает на вход
# неопределенное количество именных аргументов и
# выводит словарь с ключами удвоенно длины. {‘abc’:
# 5} -> {‘abcabc’: 5}


def main():
    my_func = lambda **x: {k*2: v for k, v in x.items()}
    print(my_func(maks='lopuh', chitat='vnimatelno'))

if __name__ == "__main__":
    main()
