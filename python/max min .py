#
# 2. Write a program that defines functions to find the sum, maximum and minimum values
# in a list of numbers.


def find_sum(numbers):
    """
    Find the sum of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(numbers)


def find_max(numbers):
    """
    Find the maximum value in a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The maximum value in the list.
    """
    if not numbers:
        return None
    return max(numbers)


def find_min(numbers):
    """
    Find the minimum value in a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The minimum value in the list.
    """
    if not numbers:
        return None
    return min(numbers)


# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
total = find_sum(numbers)
maximum = find_max(numbers)
minimum = find_min(numbers)

print(f"List: {numbers}")
print(f"Sum: {total}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
