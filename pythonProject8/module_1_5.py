immutable_var = 1, 2, 3, 'a', 'b', 'Hey'
print(immutable_var)   #кортежи данного типа не изменяемы
mutable_list = ([1, 2, 3])
mutable_list[0] = 8
print(mutable_list)