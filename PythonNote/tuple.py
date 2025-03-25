element = ('1', True, 17, ('1', False, -17))
print(id(element))
print(type(element))
print(element[3][1])
print(element.index(True))
print(element.count('1'))
print(len(element))
print(len(element[3]), '\n')

element2 = ('1', True, False, [1, 2, 3, 2, 1], 17)
element2[3][2] = 0
print(element2)
