# Дан текстовый фа л, содержащи различные даты.
# Каждая дата - это число, месяц и год. На ти самую
# раннюю дату.


from datetime import datetime

def main():
    dates = []
    with open ('time.txt', 'r') as textfile:
        for item in textfile:
            date = datetime.strptime(item.rstrip('\n'), '%Y/%m/%d').date()
            dates.append(date)

    early_date = dates[0]
    for date in dates:
        if date < early_date:
            early_date = date
    print(early_date)
if __name__ == '__main__':
    main()
