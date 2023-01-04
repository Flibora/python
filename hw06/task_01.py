from typing import Union

def convSmToInches(chislo: Union[int, float]) -> float:
    """Function for convert sm to Inches"""

    return chislo * 0.39

def convInchesToSm(chislo: Union[int, float]) -> float:
    """Function for convert inches to sm"""

    return chislo * 2.54

def convMilesToKilometers(chislo: Union[int, float]) -> float:
    """Function for convert miles to km"""

    return chislo * 1.609344

def convKiometrsToMiles(chislo: Union[int, float]) -> float:
    """Function for convert km to miles"""

    return chislo * 0.621371

def convFuntsToKilograms(chislo: Union[int, float]) -> float:
    """Function for convert funts to kilograms"""

    return chislo * 0.45359237

def convKilogramsToFunts(chislo: Union[int, float]) -> float:
    """Function for convert kilograms to funts"""

    return chislo * 2.20462262185

def convUnciiToGrams(chislo: Union[int, float]) -> float:
    """Function for convert uncii to grams"""

    return chislo * 28.34952

def convGramsToUncii(chislo: Union[int, float]) -> float:
    """Function for convert grams to uncii"""

    return chislo / 28.34952

def convGallonsToLitres(chislo: Union[int, float]) -> float:
    """Function for convert sm to Inches"""

    return chislo * 0.264172

def convLitresToGallons(chislo: Union[int, float]) -> float:
    """Function for convert sm to Inches"""

    return chislo * 3.785412

def convLitresToPinta(chislo: Union[int, float]) -> float:
    """Function for convert litres to pinta"""

    return chislo * 0.5683

def convPintToLitres(chislo: Union[int, float]) -> float:
    """Function for convert pinta to litres"""

    return chislo * 0.473176

def main():
    """The main module of the program"""

    while True:
        print('Выберите варинаты конвертирования:')
        print("1.Сантиметры в дюймы\n"
              "2.Дюймы в сантиметры\n"
              "3.Мили в километры\n"
              "4.Километры в мили\n"
              "5.Фунты в килограммы\n"
              "6.Килограммы в фунты\n"
              "7.Унции в граммы\n"
              "8.Граммы в унции\n"
              "9.Галлон в литры\n"
              "10.Литры в галлоны\n"
              "11.Пинты в литры\n"
              "12.Литры в пинты")
        punkt = int(input())
        print('Введите значение')
        chislo = int(input())
        list = [
        convSmToInches,
        convInchesToSm,
        convMilesToKilometers,
        convKiometrsToMiles,
        convFuntsToKilograms,
        convKilogramsToFunts,
        convUnciiToGrams,
        convGramsToUncii,
        convGallonsToLitres,
        convLitresToGallons,
        convLitresToPinta,
        convPintToLitres]
        if  1<= punkt <= 12:
            print(list[punkt-1](chislo))
        elif punkt == 0:
            break
        else:
            print('Введите другое число')


if __name__ == "__main__":
    main()
