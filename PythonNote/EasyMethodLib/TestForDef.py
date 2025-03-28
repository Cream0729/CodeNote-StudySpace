# A function to print multiplication table from start to end
def dTable(start, end):
    """
    Prints the multiplication table from start to end.

    Args:
        start (int): The starting number of the multiplication table.
        end (int): The ending number of the multiplication table.

    Returns:
        str: A message indicating the completion of the table printing.
    """
    for y in range(start, end + 1):
        for x in range(start, y + 1):
            print(f"{x}x{y}={x*y}", end='\t')
        print()
    return "\nFinish\n"

if __name__ == "__main__":
    print(dTable(1, 9))


# A function that takes another function as an argument and performs some calculations
def test(function, x, y):
    """
    Performs a calculation using a provided function and some additional operations.

    Args:
        function (callable): A function that takes two arguments and returns a value.
        x (int): The first input value for the provided function.
        y (int): The second input value for the provided function.

    Returns:
        float: The result of the calculation.
    """
    ans = (function(x, y) + x) * y
    ans /= 2
    return ans * 1.1

if __name__ == "__main__":
    print(test(lambda x, y: x * y / 2, 10, 7), '\n')


# A recursive function that sums numbers from start to times, Tips: the defult val must be the end of.
def fnct(start, times, ans=0):
    """
    Recursively sums numbers from start to times.

    Args:
        start (int): The current number in the summation sequence.
        times (int): The target number to sum up to.
        ans (int, optional): The accumulated sum. Defaults to 0.

    Returns:
        int: The sum of numbers from start to times.
    """
    if start != times:
        start += 1
        ans += start
        return fnct(start, times, ans)
    return ans

if __name__ == "__main__":
    print("fnct(0, 100) will return:", fnct(0, 100))
