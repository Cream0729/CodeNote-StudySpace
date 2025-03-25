# case 1: print(element)
# The element can be of type int, float, list, boolean, or others.
# For example, you can use str(normal) in it:
print("Hello! My world! Here is Python!")
print("Hello!", "My world!", "Here is Python!")
print()

# If you do not want a newline at the end, you can use end='' to prevent it:
print("Hello!", end=' ')
print("My world!", end=' ')
print("The wonderful world!")
print()

# You can also use identifiers:
i = 17
s = "cjf"
print(s, i)
print()

# You can even use operators inside print statements or parentheses:
number1 = 10
number2 = 5
ads = number1 + number2
rds = number1 - number2
print("ads:", ads, "rds:", rds)
print(number1, "*", number2, "=", number1 * number2)
print()

# If you want to make it more readable, try using formatted strings:
print(f"number1: {number1}; number2: {number2}")
print("%i / %i = %i" % (number1, number2, number1 / number2))
print()

# May when you wanner print much times, you can:
print("I'm enjoy it!\n" * 5)
print()

# How can we get an element's type or ID? We can see the value when we use the element, such as:
gS = "My name"
print(gS)  # This will print the value of gS, which is "My name"
print(id(gS))  # This will get the ID of gS
print(type(gS))  # This will get the type of gS
print()

# Also, we can do it:
gB = True
gI = 19
gF = 3.1415926
print(type(gB), type(gI), type(gS), "\n")

# How can we exchange these type? we can use <type>(element):
print(int(gF), type(int(gF)))   # It'll remove decimal's value
print(str(gI), type(str(gI)))
print(int(gB), type(int(gB)))   # Tips: True = 1, Fales = 0
print()

# Use split to get word:
s = "Hello! My world! Here is Python!"
for x in s.split(' '):
    print(x)    # .split will return a list
print()
