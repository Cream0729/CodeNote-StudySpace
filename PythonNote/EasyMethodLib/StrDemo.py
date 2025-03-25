s = "Oh, I'm enjoy Python!"

# Case 1: Get information from the string
print(len(s))  # Get the length of the string
print(s.count('o'))  # Count occurrences of 'o' in the string
print('\n', s.replace("Oh, ", ''))  # Replace "Oh, " with an empty string
print(s, '\n')  # Note: The default behavior of print() adds a newline at the end


# Example: Function definition and call
def ezp(s):
    s = "hello?"
    print(s)  # This will print "hello?" when the function is called


ezp(s)  # Call the function with s as an argument
print(s)  # Print s again to show it remains unchanged outside the function


# Also, we can use list's attributes
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s.split(' ')[0].replace(",", ''))
