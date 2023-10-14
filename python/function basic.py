# 1. Write a program that defines functions for basic mathematical operations (addition,
# subtraction, multiplication, and division). Allow the user to input two numbers and
# select an operation to perform. Use separate functions for each operation.

def add(a, b):
  """Adds two numbers together.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The sum of a and b.
  """

  sum = a + b
  return sum

def subtract(a, b):
  """Subtracts two numbers.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The difference of a and b.
  """

  difference = a - b
  return difference

def multiply(a, b):
  """Multiplies two numbers together.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The product of a and b.
  """

  product = a * b
  return product

def divide(a, b):
  """Divides two numbers.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The quotient of a and b.
  """

  quotient = a / b
  return quotient

def main():
  """Prompts the user to input two numbers and select an operation to perform."""

  # Get the two numbers from the user
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  # Get the operation from the user
  operation = input("Select an operation (+, -, *, /): ")

  # Perform the operation and display the result
  if operation == "+":
    result = add(num1, num2)
  elif operation == "-":
    result = subtract(num1, num2)
  elif operation == "*":
    result = multiply(num1, num2)
  elif operation == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operation.")
    return

  print("The result is:", result)

if __name__ == "__main__":
  main()
