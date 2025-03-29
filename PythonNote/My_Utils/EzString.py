def reverse_str(s):
    """
    :param s:   传入字符串
    :return 反转后的字符串:
    """
    return s[::-1]


def substr(string, start, end, step=1):
    """
    :param string: 传入的字符串
    :param start: 切片开始下标
    :param end: 切片结束下标
    :param step: 步过下标 < 默认 1 >
    :return 切片结果:
    """
    return string[start:end:step]

if __name__ == '__main__':
    print(reverse_str("!olleH"))
    print(substr("weishenme?", 0, 7, 2))