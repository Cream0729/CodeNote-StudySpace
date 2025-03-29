import winsound


class S:
    SN = None
    SG = None
    SA = None

    def cc(self, msg):
        print('say', self.SN, msg)

    def rang(self):
        winsound.Beep(2000, 3000)


ss = S()
ss.SA = 'a'
ss.SG = 'b'
ss.SN = 'c'
print(ss.SA, ss.SG, ss.SN)
print(ss)   # 无__str__
ss.cc('non\n')
# ss.rang()


# ================================================================================ #


class CG:
    name = None
    age = None
    gender = None

    # __xxx__ 在Python中被称为魔术方法

    def __init__(self, name, age, gender):  # 构造方法
        self.name = name
        self.age = age
        self.gender = gender
        print("Create successfull")

    def __str__(self):      # 相当于toString
        return f"name = {self.name}, age = {self.age}, gender = {self.gender}"

    def __lt__(self, other):    # 相当于comparTo
        return self.age < other.age  # (T/F)

    def __le__(self, other):
        return self.age <= other.age  # (1,0,-1)

    def __eq__(self, value):    # 相当于equals
        return self.name == value.name


cg = CG('a', 'b', 'c')
print(cg)


# ================================================================================ #


class priv:
    __Name = None   # 私有属性，子类也无法使用
    __Age = None
    __Gender = None

    def __init__(self, name, age, gender):
        self.__Name = name
        self.__Age = age
        self.__Gender = gender

    def sout(self):
        print('Hello!')

    def __str__(self):
        return f"name = {self.__Name}, age = {self.__Age}, gender = {self.__Gender}"


p = priv('a', 'b', 'c')
p.sout()
print('\n', p)


# ================================================================================ #


class PrivExtend(priv):  # 继承父类
    pass  # 直接继承父类的所有属性和方法


pv = PrivExtend('a', 'b', 'c')
pv.sout()
print(pv)


class PrEt2(priv):
    # 一般优先级由左到右递减
    def __init__(self, n, a, g):
        super().__init__(n, a, g)  # 调用父类的构造函数

    def sout(self):  # 重写方法
        super().sout()  # 调用父类的方法
        print('Python!')


pve = PrEt2('a', 'b', 'c')
pve.sout()
print(pve)