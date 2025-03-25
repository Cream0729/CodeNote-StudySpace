# Create an empty set
my_set = set()
print(my_set, '\n')

# Add an element to the set
my_set.add("Hello")
print(my_set, '\n')  # The set will not be empty after adding an element

# Clear the set and add a range of numbers
my_set.clear()
for n in range(0, 11):
    my_set.add(n)

# Remove an element from the set
my_set.remove(5)
print(my_set, '\n')

# Pop an element from the set
ele = my_set.pop()
print(ele, my_set)

# Re-add 0 back to the set
my_set.add(0)
print()

# Create another set and perform set operations
new_set = set()
for n in range(5, 16):
    new_set.add(n)

print("my_set:", my_set)
print("new_set:", new_set)
print("Difference between my_set and new_set:", my_set.difference(new_set))
print("Difference between new_set and my_set:", new_set.difference(my_set))
print()

# Update the new_set by removing elements present in my_set
new_set.difference_update(my_set)
print("new_set after difference_update:", new_set, '\n')

# Print the union of both sets
print("Union of my_set and new_set:\n", my_set.union(new_set), '\n')

# Print the length of new_set
print("Length of new_set:", len(new_set), '\n')

# Print all elements in new_set
print("Elements in new_set:", end=' ')
for ele in new_set:
    print(ele, end=' ')
print()

print(max(my_set), min(my_set))
print(sorted(my_set))
print(my_set)   # Will not effect