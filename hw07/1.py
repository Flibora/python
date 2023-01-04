# Oписать функцию fact2(n), вычисляющую дво но
# факториал: n!! = 1·3·5·...·n, если n — нечетное; n!! =
# 2·4·6·...·n, если n — четное (n > 0 — параметр целого
# типа). С помощью это функции на ти дво ные
# факториалы пяти случайных целых чисел.
from functools import reduce

def fact(n: int) -> int:
    if n <=0:
        return 1
    return reduce(lambda x,n: n*x, range(n,1,-2))




def main():
    print(fact(5))
    print(fact(8))
    print(fact(6))
    print(fact(-4))
    print(fact(7))


if __name__ == "__main__":
    main()
