immutable_var = tuple([1, 2, 3, 'a', 'b', 'c'])
print(immutable_var)
immutable_var[0] = 5
print(immutable_var) #в кортеже нельзя поменять элемент!
mutable_list = [1, 2, 3, 'a', 'b', 'c']
print(mutable_list)
mutable_list[5] = 'Modified'
print(mutable_list)
