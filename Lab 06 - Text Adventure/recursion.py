my_list = [70, 32, 98, 88, 92, 36, 81, 83, 87, 66]
temp = my_list[0]
print(temp)
print(my_list)
my_list[1] = my_list[0]
print(my_list)
my_list[0] = temp
print(temp)
print(my_list)