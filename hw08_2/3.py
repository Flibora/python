# Создать CSV файл с данными о ежедневно погоде за
# 10 дней для 3-х городов. Структура: Дата, Город,
# Температура, Скорость ветра.
# Создать отчетны фа л в формате CSV со структурой:
# Город, Средняя температура. Записать в него
# данные по каждому Городу. Данные в CSV файле
# должны быть отсортированы по возрастанию
# средней температуры.
# Найти среднюю погоду(скорость ветра и градусы)
# для Минск за последние 7 дней и вывести на экран.


import csv

def read_file(filecsv):
    rows = []
    with open(filecsv, 'r') as file:
        csvreader = csv.reader(file)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
        return fields, rows
<<<<<<< HEAD

=======
>>>>>>> f59b9ae5d6b520adb7ed857b49fe39633bd0cfd6
def sorted_list(fields, rows):
    sorted_fields = fields.pop(-1)
    temp_sorted = sorted(rows, key = lambda list: int(list[2]))
    sorted_list = []
    for keys in temp_sorted:
        sorted_list.append(keys[0:3])
    for key in sorted_list:
        print(key)
    return sorted_fields, sorted_list
<<<<<<< HEAD

=======
>>>>>>> f59b9ae5d6b520adb7ed857b49fe39633bd0cfd6
def write_csv(filename, fields, rows):
    with open(filename, 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
<<<<<<< HEAD

=======
>>>>>>> f59b9ae5d6b520adb7ed857b49fe39633bd0cfd6
def sorted_minsk(rows):
    list_minsk = []
    for key in rows:
        if key[1] == "Minsk":
            list_minsk.append(key)
    return list_minsk
<<<<<<< HEAD




=======
>>>>>>> f59b9ae5d6b520adb7ed857b49fe39633bd0cfd6
def main():
    fields, rows =read_file('statistics.csv')
    sorted_fields, sorted_rows = sorted_list(fields, rows)
    write_csv('temp_file.csv', fields, sorted_rows)
    minsk_rows = sorted_minsk(rows)
    average_temp = 0
    average_speed = 0
    for row in minsk_rows:
        average_temp+= int(row[2])
        average_speed+= int(row[3])
        if row == minsk_rows[-1]:
             average_temp/= len(minsk_rows)
             average_speed/= len(minsk_rows)
    print(f"Средняя температура по Минску за 7дней: {int(average_temp)}\n"
          f"Средняя скорость ветра по Минску за 7дней: {int(average_speed)}")


if __name__ == '__main__':
    main()
