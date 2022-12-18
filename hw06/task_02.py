import task_01

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
    if  1<= punkt <= 12:
        list = [
        task_01.convSmToInches(chislo),
        task_01.convInchesToSm(chislo),
        task_01.convMilesToKilometers(chislo),
        task_01.convKiometrsToMiles(chislo),
        task_01.convFuntsToKilograms(chislo),
        task_01.convKilogramsToFunts(chislo),
        task_01.convUnciiToGrams(chislo),
        task_01.convGramsToUncii(chislo),
        task_01.convGallonsToLitres(chislo),
        task_01.convLitresToGallons(chislo),
        task_01.convLitresToPinta(chislo),
        task_01.convPintToLitres(chislo)
    ]
        print(list[punkt-1])
    elif punkt == 0:
        break
    else:
        print('Введите другое число')
