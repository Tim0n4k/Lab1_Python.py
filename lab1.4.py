my_dict = {'a':50, 'b':5, 'c': 56,'d':4, 'e':58, 'f': 20}
print(my_dict)
dict_sort = sorted(my_dict, key=my_dict.get)
print(dict_sort)

for i in range(0, 3):
    print(dict_sort[i], ":", my_dict[dict_sort[i]])



