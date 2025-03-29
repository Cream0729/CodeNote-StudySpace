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

# Tips: defult element must be the last one


def t_ret(ts1, ts2, ts3='null'):
    return ts1, ts2, ts3


print(type(t_ret("1", "2")))
x, y, z = t_ret(ts2=10, ts1=15)
print("X :", x, ", Y:", y, ", Z:", z, '\n')


def un_nts(*args):
    print(args)
    return type(args)


print(un_nts("nihao", 1, 17, [1, 2, 3]), '\n')


def un_dts(**k_v):
    print(k_v)
    return type(k_v)


print(un_dts(a=1, b=2, c=3), '\n')


def c1(c2):
    print(c2(10, 9))


def c2(a, b):
    return a+b


c1(c2)


def cad(function):
    print(function(4, 2))


cad(lambda x, y: x * y)