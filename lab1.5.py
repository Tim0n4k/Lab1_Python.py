"""
Реализуйте программу «Магазин игрушек», которая будет
включать в себя шесть пунктов меню. У вас есть словарь, где ключ –
название игрушки. Значение – список, который содержит состав
игрушки, цену и кол-во (шт),которое есть в магазине.
1. Просмотр описания: название – описание
2. Просмотр цены: название – цена.
3. Просмотр количества: название – количество.
4. Всю информацию.
5. Покупка
В пункте «Покупка» необходимо совершить покупку, с
клавиатуры вводите название игрушки и его кол-во, n – выход из
программы. Посчитать цену выбранных товаров и сколько товаров
осталось в изначальном списке.
6. До свидания – 2 балла
"""


toys = {
    "Машинка" : ["металл и пластик", 120, 64],
    "Кукла" : ["текстиль и пластик", 50, 23],
    "Конструктор" : ["пластик", 85, 17],
    "Пазлы" : ["картон", 25, 44],
    "Робот" : ["металл и электроника", 155, 6],
}

copy_toys = {
    "Машинка" : ["металл и пластик", 120, 64],
    "Кукла" : ["текстиль и пластик", 50, 23],
    "Конструктор" : ["пластик", 85, 17],
    "Пазлы" : ["картон", 25, 44],
    "Робот" : ["металл и электроника", 155, 6],
}

"""
toys = {
    "Машинка" : ["металл и пластик", 2100, 500],
    "Кукла" : ["текстиль и пластик", 5120, 203],
    "Конструктор" : ["пластик", 8045, 107],
    "Пазлы" : ["картон", 2015, 404],
    "Робот" : ["металл и электроника", 1505, 641],
}

copy_toys = {
    "Машинка" : ["металл и пластик", 2100, 500],
    "Кукла" : ["текстиль и пластик", 5120, 203],
    "Конструктор" : ["пластик", 8045, 107],
    "Пазлы" : ["картон", 2015, 404],
    "Робот" : ["металл и электроника", 1505, 641],
}
"""

col_widths = [12, 7, 10]
count_check = 0
def display_upper_check():
    print(" _____________ЧЕК_____________ ")
    print(" _____________________________ ")
    print("|Название   |Кол-во |Стоимость|")

def display_line_check():
    print("|-----------|-------|---------|")

def display_end_check(count_check):
    print("|___________|_______|_________|")
    print(" ============================= ")
    print(f" ИТОГО: {count_check}         ")
    print(" ============================= ")

def display_upper_table():
    print(" ___________"
          "________________"
          "_______________"
          "______________"
          "_______________"
          "____________________ ")
    print("|Название   |"
          "Машинка          |"
          "Кукла              |"
          "Конструктор "
          "|Пазлы  "
          "|Робот               |")
    print("|-----------|"
          "-----------------"
          "|-------------------"
          "|------------"
          "|-------"
          "|--------------------|")

def display_line_table():
    print("|-----------"
          "|-----------------"
          "|-------------------"
          "|------------"
          "|-------"
          "|--------------------|")

def display_end_table():
    print("|___________"
          "|_________________"
          "|___________________"
          "|____________"
          "|_______"
          "|____________________|")

def display_description(toys):
    print(f"|Описание   |"
          f"{toys['Машинка'][0]} |"
          f"{toys['Кукла'][0]} |"
          f"{toys['Конструктор'][0]}     |"
          f"{toys['Пазлы'][0]} |"
          f"{toys['Робот'][0]}|")

def display_amount(toys):
    print(f"|Количество |"
          f"{toys['Машинка'][2]}               |"
          f"{toys['Кукла'][2]}                 |"
          f"{toys['Конструктор'][2]}          |"
          f"{toys['Пазлы'][2]}     |"
          f"{toys['Робот'][2]}                   |")

def display_cost(toys):
    print(f"|Цена, byn  |"
          f"{toys['Машинка'][1]}              |"
          f"{toys['Кукла'][1]}                 |"
          f"{toys['Конструктор'][1]}          |"
          f"{toys['Пазлы'][1]}     |"
          f"{toys['Робот'][1]}                 |")


def clear_console():
    import os


def input_toy_and_amount():
    while True:

        toy1 = input("Введите наименование игрушки: ")
        toy1 = toy1.capitalize()
        if toy1 not in toys:
            clear_console()
            print("Такой игрушки нет. Попробуй ещё раз")
        else:
            clear_console()
            break

    while True:

        num1 = input("Введите количество игрушек, которое хотите приобрести: ")
        if not num1.isdigit():
            clear_console()
            print("Ошибка ввода. Попробуй ещё раз")
        elif int(num1) > toys[toy1][2]:
            clear_console()
            num1 = int(num1)
            print("Такого количества игрушек нет в наличии.")
            print("В наличии осталось только ", toys[toy1][2], ". Попробуйте ещё раз")
        else:
            num1 = int(num1)
            toys[toy1][2] = toys[toy1][2] - num1
            clear_console()
            print("Покупка произведена успешна. Игрушек в наличии осталось ", toys[toy1][2])
            print("Стоимость покупки составила ", num1 * toys[toy1][1], " byn")
            break

    return num1 * toys[toy1][1]

def menu0():
    print("МАГАЗИН ИГРУШЕК")
    print("1. Просмотр опис ания: название – описание")
    print("2. Просмотр цены: название – цена")
    print("3. Просмотр количества: название – количество")
    print("4. Всю информацию")
    print("5. Покупка")
    print("6. До свидания")

def menu():
    while True:
        menu0()
        num_operation = input("Введите номер операции: ")
        if not num_operation.isdigit() or num_operation not in ["1", "2", "3", "4", "5", "6"]:
            clear_console()
            print("Ошибка ввода. Попробуй ещё раз")
        else:
            num_operation = int(num_operation)
            break
    return num_operation

def count_space_column1(name):
    result = ' '*(col_widths[0] - len(name) - 1)
    return result

def count_buy_toys(name):
    result = copy_toys[name][2] - toys[name][2]
    return result

def count_space_column2(name):
    result = ' '*(col_widths[1] - len(str(count_buy_toys(name))))
    return result

def full_cost_buy_toys(name):
    result1 = count_buy_toys(name) * copy_toys[name][1]
    return result1

def count_space_column3(name):
    result = ' '*(col_widths[2] - 1 - len(str(full_cost_buy_toys(name))))
    return result

def counting_check(name, sum):
    sum = sum + full_cost_buy_toys(name)

while True:

    num_operation = menu()
    clear_console()
    if num_operation == 1:
        display_upper_table()
        display_description(toys)
        display_end_table()
    elif num_operation == 2:
        display_upper_table()
        display_cost(toys)
        display_end_table()
    elif num_operation == 3:
        display_upper_table()
        display_amount(toys)
        display_end_table()
    elif num_operation == 4:
        display_upper_table()
        display_amount(toys)
        display_line_table()
        display_cost(toys)
        display_line_table()
        display_description(toys)
        display_end_table()

        display_upper_table()
        display_amount(copy_toys)
        display_line_table()
        display_cost(copy_toys)
        display_line_table()
        display_description(copy_toys)
        display_end_table()
    elif num_operation == 5:
        sum_cost = 0
        sum_cost = input_toy_and_amount() + sum_cost
        while True:
            choice = input("Хотите ли еще купить игрушек? ")
            if choice.lower() == "да" or choice.lower() == "yes":
                clear_console()
                sum_cost = sum_cost + input_toy_and_amount()
            elif choice.lower() == "нет" or choice.lower() == "no":
                clear_console()
                print("Спасибо за покупки !!!")
                print("Общая стоимость всех игрушек составляет ", sum_cost, " byn")
                break
            else:
                clear_console()
                print("Ошибка ввода. Попробуй ещё раз")
    elif num_operation == 6:
        display_upper_check()
        if count_buy_toys("Машинка")!=0:
            display_line_check()
            print(f"|Машинка{count_space_column1("Машинка")}|{count_buy_toys("Машинка")}{count_space_column2("Машинка")}|"
                  f"{full_cost_buy_toys("Машинка")}{count_space_column3("Машинка")}|")
            count_check = count_check + full_cost_buy_toys("Машинка")
        if count_buy_toys("Кукла")!=0:
            display_line_check()
            print(f"|Кукла{count_space_column1("Кукла")}|{count_buy_toys("Кукла")}{count_space_column2("Кукла")}|"
                  f"{full_cost_buy_toys("Кукла")}{count_space_column3("Кукла")}|")
            count_check = count_check + full_cost_buy_toys("Кукла")
        if count_buy_toys("Конструктор")!=0:
            display_line_check()
            print(f"|Конструктор{count_space_column1("Конструктор")}|{count_buy_toys("Конструктор")}{count_space_column2("Конструктор")}|"
                  f"{full_cost_buy_toys("Конструктор")}{count_space_column3("Конструктор")}|")
            count_check = count_check + full_cost_buy_toys("Конструктор")
        if count_buy_toys("Пазлы")!=0:
            display_line_check()
            print(f"|Пазлы{count_space_column1("Пазлы")}|{count_buy_toys("Пазлы")}{count_space_column2("Пазлы")}|"
                  f"{full_cost_buy_toys("Пазлы")}{count_space_column3("Пазлы")}|")
            count_check = count_check + full_cost_buy_toys("Пазлы")
        if count_buy_toys("Робот")!=0:
            display_line_check()
            print(f"|Робот{count_space_column1("Робот")}|{count_buy_toys("Робот")}{count_space_column2("Робот")}|"
                  f"{full_cost_buy_toys("Робот")}{count_space_column3("Робот")}|")
            count_check = count_check + full_cost_buy_toys("Робот")
        display_end_check(count_check)

        print("До свидания!!!")
        exit()
















"""
    print(" ___________________________________________________________________________________________ ")
    print("|Название   |Машинка          |Кукла              |Конструктор |Пазлы  |Робот               |")
    print("|-----------|-----------------|-------------------|------------|-------|--------------------|")
    print("|Количество |64               |23                 |17          |44     |6                   |")
    print("|-----------|-----------------|-------------------|------------|-------|--------------------|")
    print("|Цена, byn  |120              |50                 |85          |25     |155                 |")
    print("|-----------|-----------------|-------------------|------------|-------|--------------------|")
    print("|Описание   |Металл и пластик |Текстиль и пластик |Пластик     |Kартон |Mеталл и электроника|")
    print("|___________|_________________|___________________|____________|_______|____________________|")
"""

"""
    print(" _____________ЧЕК_____________ ")
    print(" _____________________________ ")
    print("|Название   |Кол-во |Стоимость|")
    print("|-----------|-------|---------|")
    print("|Машинка    |64     |23       |")
    print("|-----------|-------|---------|")
    print("|Кукла      |120    |50       |")
    print("|-----------|-------|---------|")
    print("|Конструктор|64     |23       |")
    print("|-----------|-------|---------|")
    print("|Пазлы      |120    |50       |")
    print("|-----------|-------|---------|")
    print("|Робот      |       |         |")
    print("|___________|_______|_________|")
    print("||===========================||")
    print("||ИТОГО:                     ||")
    print("||===========================||")
    

"""