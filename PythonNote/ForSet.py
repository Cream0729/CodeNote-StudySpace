my_set = set()  # get a none setlist
print(my_set)

my_set.add("Hello")
print(my_set)   # If add element will not null

my_set.clear()
for n in range(0, 10):
    my_set.add(n)

my_set.remove(5)
print(my_set)
ele = my_set.pop()
print(ele, my_set)
my_set.add(0)

new_set = set()
for n in range(5, 16):
    new_set.add(n)

print(my_set)
print(new_set)
print(my_set.difference(new_set), new_set.difference(my_set))
