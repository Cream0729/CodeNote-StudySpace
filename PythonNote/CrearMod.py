__all__ = ['ac_Table', 'get_table']

def ac_Table(start, length):
    print()
    for y in range(start, length + 1):
        for x in range(start, y + 1):
            print(f"{x}×{y}={x*y}", end='\t')
        print()
    return "Finish"


# Tables
def get_table(start, length):
    """
    打印从指定起始值到目标值的乘法表，并返回结束信息。

    :param start: 乘法表的起始值。
    :param length: 乘法表的目标结束值。

    :return str: 当达到目标值时返回"Print Finish!"，否则递归调用自身。

    示例:
        >>> print(get_table(2, 9))
        1×1=1
        1×2=2	2×2=4
        ...
        1×9=9	2×9=18	...	9×9=81
        Print Finish!

    注:
        该函数使用递归实现，如果length值较大，可能会触发Python的递归深度限制。
    """
    global num
    num = 10
    print()
    start = int(start)
    length = int(length)

    for y in range(1, start + 1):
        for x in range(1, y + 1):
            print(f"{x}×{y}={x*y:<2}", end='\t')
        print()

    if start == length:
        return "--- Finish! ---"

    return get_table(start + 1, length)

def sayHello():
    print("Hello!")

 
#It will be use here
if __name__ == '__main__':
    ac_Table(-3, 4)