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
import write_read_csv

def sorted_list(fields, rows):
    sorted_fields = fields[1:-1]
    filt_minsk = list(filter(lambda row: row[1] == 'Minsk',rows))
    filt_pinsk = list(filter(lambda row: row[1] == 'Pinsk',rows))
    filt_vitebsk = list(filter(lambda row: row[1] == 'Vitebsk',rows))
    return sorted_fields,filt_minsk, filt_pinsk, filt_vitebsk

def average_city_info(rows):
    average_temp= 0
    average_speed = 0
    for row in rows:
        average_temp+=int(row[2])
        average_speed+=int(row[3])
        if row == rows[-1]:
            average_temp/= len(rows)
            average_speed/= len(rows)
    return average_temp, average_speed

def write_info_csv(filename, fields, rows):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

def main():
    fields, rows =write_read_csv.read_csv('statistics.csv')
    sorted_fields, minsk, pinsk, vitebsk = sorted_list(fields, rows)
    minsk_temp, minsk_wind = average_city_info(minsk)
    pinsk_temp, pinsk_wind = average_city_info(pinsk)
    vitebsk_temp, vitebsk_wind = average_city_info(vitebsk)
    sorted_rows = [["Minsk", int(minsk_temp)], ["Pinsk", int(pinsk_temp)],
                   ["Vitebsk", int(vitebsk_temp)]]
    write_info_csv('info_temp.csv', sorted_fields, sorted_rows)
    print(f"Средняя температура по Минску за 7дней: {int(minsk_temp)}\n"
          f"Средняя скорость ветра по Минску за 7дней: {int(minsk_wind)}")


if __name__ == '__main__':
    main()
