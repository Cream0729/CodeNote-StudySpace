import time


f = open("T:/功能总览.txt", "r", encoding="UTF-8")
print("\n===========================================\n")
print(type(f), '\n')
print(f.read())  # If element is null, it will get all bytes.
print("\n===========================================\n")

f = open("T:/功能总览.txt", "r", encoding="UTF-8")
print(f.read(100))
print("\n===========================================\n")

# Read Lines
f = open("T:/功能总览.txt", "r", encoding="UTF-8")
lines = f.readlines()   # return list
print(lines)
print("\n===========================================\n")

with open("T:/功能总览.txt", "r", encoding="UTF-8") as f:
    for line in f:  # read times by a line
        print(line, end='')
print("\n===========================================\n")

lable = ''
print("Count '" + lable + "' times:",
      (open("T:/功能总览.txt", "r", encoding="UTF-8").read()).count(lable))
print("\n===========================================\n")

(open("T:/test.txt", 'w', encoding="UTF-8")).write("Hello World !")
print("Finish")

print("\n===========================================\n")

(open("T:/test.txt", 'a', encoding="UTF-8")).write("\nIt's Python !")
print("Finish")

print("\n===========================================\n")
