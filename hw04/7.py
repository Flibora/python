''' В семье N свадьба. Они решили выбрать заведение, где будут праздновать в
зависимости от количества люде , которое прибудет к утру. Если их будет больше
50 - закажут ресторан, если от 20 до 50 -то кафе, а если меньше 20 то отпраздную
дома. Вывести "ресторан", "кафе", "дом" в зависимости от количества гостей .'''

number_family = int(input())

if number_family  > 50:
    print("закажем ресторан")
elif 20 <= number_family <= 50:
    print("закажем кафе")
else:
    print("будем дома")
