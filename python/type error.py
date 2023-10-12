# Write a program to perform an operation between two data types that are not
# compatible (e.g., adding a string and an integer). The program need to handle
# theTypeError` and print a suitable error message.
#
try:
    result="python"+38
    print(f"result{result}")
except TypeError:
    print("An operrtion between two data types that are not compatible")
