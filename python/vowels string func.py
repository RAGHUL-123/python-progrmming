# 3. Write a program that defines function to;
# a. count the number of vowels in a given string,
# b. length of the string
# c. to reverse the string.
# Test these functions.
def count_vowels(input_string):
    """
    Count the number of vowels in a given string.

    Args:
        input_string (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = "AEIOUaeiou"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count


def string_length(input_string):
    """
    Find the length of a given string.

    Args:
        input_string (str): The input string.

    Returns:
        int: The length of the string.
    """
    return len(input_string)


def reverse_string(input_string):
    """
    Reverse a given string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The reversed string.
    """
    return input_string[::-1]


# Test the functions
input_str = "Hello, World!"
vowel_count = count_vowels(input_str)
length = string_length(input_str)
reversed_str = reverse_string(input_str)

print(f"Input String: {input_str}")
print(f"Number of Vowels: {vowel_count}")
print(f"Length of the String: {length}")
print(f"Reversed String: {reversed_str}")
