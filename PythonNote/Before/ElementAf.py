from typing import Union


my_list: list[int] = [1, '10', 9]   # 只是一个注解，不会限制
print(my_list)
my_list += '1是'
print(my_list)

# Union：指联合类型
new_list: list[list, Union[str, int]] = [1, '10', 10]
