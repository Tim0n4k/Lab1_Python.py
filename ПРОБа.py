toys = {
    "Машинка": ["металл и пластик", 120, 64],
    "Кукла": ["текстиль и пластик", 50, 23],
    "Конструктор": ["пластик", 85, 17],
    "Пазлы": ["картон", 25, 44],
    "Робот": ["металл и электроника", 155, 6],
}

# Заголовки таблицы
headers = ["Название", "Описание", "Цена, byn", "Количество"]

# Вывод таблицы
print(" " + "_" * 93)
print("|" + "|".join(f"{header:<15}" for header in headers) + "|")
print("|" + "-" * 93 + "|")

# Вывод данных
for toy, details in toys.items():
    description, price, quantity = details
    print(f"|{toy:<15}|{description:<17}|{price:<12}|{quantity:<10}|")
    print("|" + "-" * 93 + "|")

print(" " + "‾" * 93)
toys = {
    "Машинка": ["металл и пластик", 120, 64],
    "Кукла": ["текстиль и пластик", 50, 23],
    "Конструктор": ["пластик", 85, 17],
    "Пазлы": ["картон", 25, 44],
    "Робот": ["металл и электроника", 155, 6],
}

# Заголовки таблицы
headers = ["Название", "Описание", "Цена, byn", "Количество"]

# Ширина столбцов
col_widths = [15, 20, 12, 12]

# Вывод таблицы
print(" " + "_" * (sum(col_widths) + len(col_widths) + 1))
print("|" + "|".join(f"{header:<{col_widths[i]}}" for i, header in enumerate(headers)) + "|")
print("|" + "-" * (sum(col_widths) + len(col_widths) + 1) + "|")

# Вывод данных
for toy, details in toys.items():
    description, price, quantity = details
    print(f"|{toy:<{col_widths[0]}}|{description:<{col_widths[1]}}|{price:<{col_widths[2]}}|{quantity:<{col_widths[3]}}|")
    print("|" + "-" * (sum(col_widths) + len(col_widths) + 1) + "|")

print(" " + "‾" * (sum(col_widths) + len(col_widths) + 1))