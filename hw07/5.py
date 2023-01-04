# Дан список строк. Отформатировать все строки в
# формате ‘{i} - {string}’, где i это порядковы номер
# строки в списке. Использовать генератор списков.

def main():
    """the idea of this function is to add index of the list in string """
    # list_str = ['fdgdf', 'jfdgkw', 'jidfgjow']
    # new_list = list(map(lambda x: f'{str(list_str.index(x))} - {x}', list_str))
    # print(new_list)

    list_str = ['fdgdf', 'jfdgkw', 'jidfgjow']
    new_list = [f'{list_str.index(x)} - {x}' for x in list_str]
    print(new_list)


if __name__ == "__main__":
    main()
