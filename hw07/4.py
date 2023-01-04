# Вычислить значения нижеприведенной функции в
# диапазоне значений x от -10 до 10 включительно с
# шагом, равным 1.
# y = x2 при -5 <= x <= 5;
# y = 2*|x|-1 при x < -5;
# y = 2x при x > 5.
# В качестве результат вывести на экран значение
# функции y при каждом x из указанного диапазона.

def func(num1:int, num2:int) -> list:
    result1 = list(map(lambda x: x**2, range(num1, num2+1)))
    result2 = list(map(lambda x: 2*abs(x)-1, range(num1-1,num2)))
    result3 = list(map(lambda x: 2*x, range(num1-1, num2 + 1)))
    return (result1, result2, result3)


def main():
    num1 = int(input())
    num2 = int(input())
    result = func(num1, num2)
    for x in result:
        print(x)


if __name__ == "__main__":
    main()
