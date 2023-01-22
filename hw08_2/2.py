# Создать CSV фа л с данными следующе структуры:
# Имя, Фамилия, Возраст. Создать отчетны фа л в
# формате CSV с информацие по количеству люде
# входящих в ту или иную возрастную группу.
# Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.

import csv


def sorted_list(rows):
    ages_categ = [0,0,0,0,0]
    for row in rows:
        if int(row[2]) <= 12:
            ages_categ[0] += 1
        elif int(row[2])>=13 and int(row[2])<=18:
            ages_categ[1] += 1
        elif int(row[2])>=19 and int(row[2])<=25:
            ages_categ[2] += 1
        elif int(row[2])>=26 and int(row[2])<=40:
            ages_categ[3] +=1
        else: ages_categ[4]+=1
    return ages_categ

def read_csv(filename):
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return fields, rows

def write_csv(filename, fields, rows):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerow(rows)

def write_sotred_csv(filename, rows):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)

def prepare_csv_data(fields, rows):
    list_fields = fields.split(',')
    list_rows = []
    for row in rows:
        list_rows.append(row.split(','))
    return list_fields, list_rows


def main():
    file_fields, file_rows = read_csv('file_csv.csv')
    ages_list = sorted_list(file_rows)
    new_fields = ['1-12', '13-18', '19-25', '26-40', '40+']
    write_csv('sorted_file.csv', new_fields, ages_list)


if __name__ == '__main__':
    main()
