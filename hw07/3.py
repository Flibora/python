# Описать функцию для перевода десятичного числа в
# двоичное. Описать бесконечный цикл, в котором
# запрашивать у пользователя число и переводить его в
# двоичную систему. Признак окончания работы
# программы - введенное пользователем число 0.
# Подсказка: числа в двоичной системе хранить как
# строки.

def convert(num: int) -> str:
    binary_num: str = ''
    while num > 0:
        binary_num += str(num % 2)
        num = num // 2
    binary_num =binary_num[::-1]
    return binary_num

def main():
    while True:
        number = int(input())
        if not number :
            return
        print(convert(number))

if __name__ == "__main__":
    main()
