cort = (12, 34, 45, 56, 68, 1, 23, 56, 45)
s = 0
for i in range(1, len(cort), 2):
    s = s + cort[i]
    if i!=len(cort)-2:
        print(cort[i], end = " + ")
    else:
        print(cort[i], end=" = ")

print(s)

print("Hello")