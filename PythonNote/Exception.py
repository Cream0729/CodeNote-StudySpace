try:
    print(name)
except NameError:
    print("Error")

try:
    print(1/0)
    print(name)
except (NameError, ZeroDivisionError) as e:
    print(e)
else:
    print("Have not error")
finally:
    print("Finish")