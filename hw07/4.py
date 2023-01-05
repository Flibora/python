# Вычислить значения нижеприведенной функции в
# диапазоне значений x от -10 до 10 включительно с
# шагом, равным 1.
# y = x2 при -5 <= x <= 5;
# y = 2*|x|-1 при x < -5;
# y = 2x при x > 5.
# В качестве результат вывести на экран значение
# функции y при каждом x из указанного диапазона.

def func(num1:int, num2: int) -> list:
    list = []
    for x in range(num1, num2):
        if x<-5:
            y = 2*abs(x)-1
            list.append(y)
        elif -5<=x and x<=5:
            y = x**2
            list.append(y)
        else :
            y = 2*x
            list.append(y)
    return list


def main():
    num1 = int(input())
    num2 = int(input())
    result = func(num1, num2)
    print(result)


if __name__ == "__main__":
    main()


# def func(num1:int, num2:int) -> list:
#     result = [2*abs(x)-1 for x in range(num1, num2+1) if x<-5]
#     result +=[x**2 for x in range(num1, num2+1) if -5<=x and x<=5]
#     result +=[2*x for x in range(num1, num2+1) if x > 5]
#     return (result)
#
#
# def main():
#     num1 = int(input())
#     num2 = int(input())
#     result = func(num1, num2)
#     print(result)
