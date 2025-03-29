def printFileInfo(file, ecod="UTF-8"):
    """
    :param file: 传入的文件路径
    :param ecod: 编码格式 < 默认 UTF-8 >
    :return success/failure: 执行终态 
    """
    f = None
    try:
        f = open(file, 'r', encoding=ecod)
        info = f.read()
        print('[', file, '] -', ecod, "- Inof as: \n\n", info)
        return "success"
    except Exception as e:
        print(e)
        return "failure"
    finally:
        if f:
            f.close


def writeInfoToFile(file, ctrl=False):
    """
    :param file: 文件路径传入
    :param ctrl: 是否开启续写 < 默认 False >
    :param ecod: 编码格式 < 默认 UTF-8 >
    """
    try:
        fc = 'w'
        if (ctrl): fc = 'a'
        print("仅输入 /#?#/ 则结束写入")
        f = open(file, fc)
        while (True):
            info = input("-> | ")
            if info == "/#?#/": 
                return "finish"
            else:
                f.write(info+'\n')
    except Exception as e:
        print(e)
        return "failure"
    finally:
        f.close


def copyFileTo(fileFrom: str, fileTo: str) -> str:   # : xx 是类型注解，-> 返回值注解
    try:
        with open(fileFrom, 'rb') as from_file:
            with open(fileTo, 'wb') as to_file:
                buffer_size = 4096
                while True:
                    buffer = from_file.read(buffer_size)
                    if not buffer:
                        break
                    to_file.write(buffer)
        return "Finish"
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    printFileInfo("T:/功能总览.txt")
    #writeInfoToFile("T:/txt.txt")
    print(copyFileTo("U:/Photoshop2025.zip", "T:/copy.zip"))
