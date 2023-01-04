# Даны три слова. Выяснить, является ли хоть одно из
# них палиндромом ("перевертышем"), т. е. таким,
# которое читается одинаково слева направо и справа
# налево. (Определить функцию, позволяющую
# распознавать слова палиндромы.)

def palindrom(words):
    return list(filter(lambda name: name == name[::-1], words))


def main():
    words = ['alla', 'humster', 'illi', 'illilli']
    print(palindrom(words))

if __name__ == "__main__":
    main()
