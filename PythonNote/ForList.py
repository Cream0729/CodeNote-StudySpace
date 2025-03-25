# theList = ['a', 'b', 'c', 'd', 'e']
# for c in theList:
#     print(c, end=' ')
# print("\n", theList[3])
# print(type(theList))

# TheList = ['A', 'B', 'C', 'D', 'E']
# TheList += 'F'
# TheList -= TheList[3]

# words = [theList, TheList]
# print(words)
# print(type(words), words[0], ' ', words[0][1])

my_list = ['a', 'b', 'c', 'e', 'f']
my_list.insert(3, 'd')
print(my_list, '\n')

del my_list[5]
print(my_list)
print(my_list.pop(4))
print(my_list, '\n')

my_list.remove('a')
my_list += 'b'
my_list.append('b')
print(my_list)
print(my_list.count('b'), '\n')

my_list.extend(['h', 'i', 'j', 'k'])
print(my_list, '\n')

print(my_list[-1])
print(my_list, '\n')

my_list.clear()
print(my_list)

s = "my test for 18 len"
print(len(s))
print(s.replace('s', 'x'))
print(s, '\n')
for sr in s.split(' '):
    print(sr)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[0:9:2])   # 起 ：终 ：步
print(my_list[::2])

my_ele = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_ele[::-1])
