
s = input("Введите строку: ")

max_count = 0
symbol = 0
max_symbol = 0
for i in range(len(s)):
    a = s[i]
    count = 0
    for j in range(len(s)):
        if s[j] == a:
            count = count + 1
            symbol = a
    if max_count < count:
        max_count = count
        max_symbol = symbol
print("Cимвол, который появляется наиболее часто ", max_symbol)
s = s[::-1]
print("Cтрокa в обратном порядке :", s)