list1 = [13,56,'Python',34,19,'love' ]
for i in range(0,len(list1)):
    if isinstance(list1[i], int):
        if list1[i] % 2 == 0:
            print("Произведение цифр равно",(list1[i]%10)*(list1[i]//10))
        else:
            list1[i] = 1
print("Изменненный список :", list1)
