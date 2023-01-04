# Даны три слова. Выяснить, является ли хоть одно из
# них палиндромом ("перевертышем"), т. е. таким,
# которое читается одинаково слева направо и справа
# налево. (Определить функцию, позволяющую
# распознавать слова палиндромы.)

def palindrom(words):
    x = list(filter(lambda name: name == name[::-1], words))
    if x:
        return print(f'Есть слова палиндромы , {x}')
    return print('нет слов')


def main():
    words = ['alla', 'humster', 'illi', 'illilli']
    print(palindrom(words))

if __name__ == "__main__":
    main()
